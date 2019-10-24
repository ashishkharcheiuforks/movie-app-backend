from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ArtistConfig(AppConfig):
    name = 'artist'
    verbose_name = _('Artist')
