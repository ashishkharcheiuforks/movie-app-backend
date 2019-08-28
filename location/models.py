from django.db import models
from django.utils.translation import ugettext_lazy as _


class Country(models.Model):
    name = models.CharField(_('Country name'), max_length=60)
    slug = models.SlugField(_('Seo link'), unique=True)

    class Meta:
        db_table = 'countries'
        ordering = ('name',)
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')

    def __str__(self):
        return self.name
