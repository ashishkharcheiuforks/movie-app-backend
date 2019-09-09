from django.db import models
from django.db.utils import ProgrammingError
from django.template.defaultfilters import truncatechars
from django.utils.translation import ugettext_lazy as _


class Parameter(models.Model):
    key = models.CharField(_('Parameter key'), max_length=32, unique=True, editable=False)
    description = models.CharField(_('Description'), max_length=255, null=True, blank=True)
    value = models.TextField(_('Parameter value'), null=True, blank=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True, null=True)

    @property
    def admin_list_value(self):
        return truncatechars(self.value, 50)

    admin_list_value.fget.description = _('Parameter value')

    class Meta:
        ordering = ('key',)
        db_table = 'parameters'
        verbose_name = _('Parameter')
        verbose_name_plural = _('Parameters')

    def __str__(self):
        return self.key

    @staticmethod
    def get_one(key):
        try:
            param = Parameter.objects.get(key=key)
            return param.value
        except (Parameter.DoesNotExist, ProgrammingError):
            return None

    @staticmethod
    def get_multiple(keys):
        result = {}
        params = Parameter.objects.filter(key__in=keys)
        for param in params:
            result[param.key] = param.value
        return result
