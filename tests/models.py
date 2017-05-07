from django.db import models

from authrole.mixins import RoleMixin


class MyUser(RoleMixin, models.Model):
    user = models.OneToOneField('auth.User', related_name='user')
