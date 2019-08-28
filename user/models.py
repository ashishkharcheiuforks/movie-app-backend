from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True, null=True, blank=True)

    class Meta(AbstractUser.Meta):
        db_table = 'users'

    def __str__(self):
        if self.first_name and self.last_name:
            return self.get_full_name()
        else:
            return self.username

    def save(self, *args, **kwargs):
        self.email = None if self.email == '' else self.email
        super().save(*args, **kwargs)
