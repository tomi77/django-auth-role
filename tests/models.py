from django.db import models


class MyUser(models.Model):
    role = models.ForeignKey('authrole.Role', related_name='myusers')
    user = models.OneToOneField('auth.User', related_name='user')
