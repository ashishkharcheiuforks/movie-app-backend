from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Avg
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _


class Genre(models.Model):
    name = models.CharField(_('Genre name'), max_length=50)
    slug = models.SlugField(_('Seo link'), unique=True)
    description = models.TextField(_('Description'), null=True, blank=True)
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)

    class Meta:
        db_table = 'genres'
        ordering = ('name',)
        verbose_name = _('Genre')
        verbose_name_plural = _('Genres')

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(_('Movie name'), max_length=150)
    slug = models.SlugField(_('Seo link'), unique=True)
    country = models.ForeignKey('location.Country', models.DO_NOTHING, verbose_name=_('Country'))
    release_date = models.DateField(_('Release date'))
    genres = models.ManyToManyField(Genre, verbose_name=_('Genres'))
    description = models.TextField(_('Description'), null=True, blank=True)
    image = models.ImageField(_('Movie image'))
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)

    @property
    def rating(self):
        return self.comment_set.filter(confirmed=True).aggregate(Avg('star'))['star__avg']

    rating.fget.short_description = _('Rating')

    @property
    def year(self):
        return self.release_date.year

    year.fget.short_description = _('Year')

    class Meta:
        db_table = 'movies'
        ordering = ('-id',)
        verbose_name = _('Movie')
        verbose_name_plural = _('Movies')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = self.generate_unique_slug() if not self.slug else self.slug
        return super().save(*args, **kwargs)

    def generate_unique_slug(self):
        # Get slug field
        slug = slugify(self.name.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Movie.objects.filter(slug=unique_slug).exclude(pk=self.pk).exists():
            unique_slug = '{}-{}'.format(unique_slug, counter)
            counter += 1
        return unique_slug


class Trailer(models.Model):
    movie = models.ForeignKey(Movie, models.CASCADE, 'trailers', verbose_name=_('Movie'))
    title = models.CharField(_('Trailer title'), max_length=160)
    video_url = models.URLField(_('Video Url'))
    release_date = models.DateField(_('Release date'))
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)

    class Meta:
        db_table = 'trailers'
        ordering = ('-movie', 'id')
        verbose_name = _('Trailer')
        verbose_name_plural = _('Trailers')

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey('user.User', models.CASCADE, verbose_name=_('User'))
    movie = models.ForeignKey(Movie, models.CASCADE, verbose_name=_('Movie'))
    comment = models.TextField(_('Comment'))
    star = models.PositiveSmallIntegerField(_('Star'), validators=[MinValueValidator(1), MaxValueValidator(10)])
    confirmed = models.BooleanField(_('Confirmed'), default=False)
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)

    class Meta:
        db_table = 'comments'
        ordering = ('-id',)
        unique_together = ('movie', 'user')
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

    def __str__(self):
        return str(self.user)


class MovieArtist(models.Model):
    movie = models.ForeignKey(Movie, models.CASCADE, verbose_name=_('Movie'))
    artist = models.ForeignKey('artist.Artist', models.CASCADE, verbose_name=_('Artist'))
    job = models.ForeignKey('artist.Job', models.CASCADE, verbose_name=_('Job'))
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)

    class Meta:
        db_table = 'movie_artist'
        ordering = ('-movie__release_date', 'id')
        unique_together = ('movie', 'artist', 'job')
        verbose_name = _('Movie & Artist')
        verbose_name_plural = _('Movie & Artists')

    def __str__(self):
        return '{} / {}'.format(self.artist, self.job)
