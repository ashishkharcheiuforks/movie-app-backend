from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ParameterConfig(AppConfig):
    name = 'parameter'
    verbose_name = _('Parameter')
