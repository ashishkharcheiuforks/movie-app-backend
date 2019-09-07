from datetime import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _


class JobCategory(models.Model):
    name = models.CharField(_('Name'), max_length=20)
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)

    class Meta:
        db_table = 'job_categories'
        ordering = ('name',)
        verbose_name = _('Job Category')
        verbose_name_plural = _('Job Categories')

    def __str__(self):
        return self.name


class Job(models.Model):
    name = models.CharField(_('Name'), max_length=20)
    slug = models.SlugField(_('Seo link'), unique=True)
    category = models.ForeignKey(JobCategory, models.SET_NULL, verbose_name=_('Category'), blank=True, null=True)
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)

    class Meta:
        db_table = 'jobs'
        ordering = ('name',)
        verbose_name = _('Job')
        verbose_name_plural = _('Jobs')

    def __str__(self):
        return self.name


class Artist(models.Model):
    first_name = models.CharField(_('First name'), max_length=50)
    last_name = models.CharField(_('Last name'), max_length=50)
    slug = models.SlugField(_('Seo link'), unique=True)
    birth_date = models.DateField(_('Birth date'), blank=True, null=True)
    image = models.ImageField(_('Image'))
    jobs = models.ManyToManyField(Job, verbose_name=_('Jobs'))
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)

    @property
    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @property
    def age(self):
        return int((datetime.now().date() - self.birth_date).days / 365.25) if self.birth_date else None

    age.fget.short_description = _('Age')

    class Meta:
        db_table = 'artists'
        ordering = ('-id',)
        verbose_name = _('Artist')
        verbose_name_plural = _('Artists')

    def __str__(self):
        return self.fullname
