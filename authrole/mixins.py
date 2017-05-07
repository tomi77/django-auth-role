from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class RoleMixin(models.Model):
    role = models.ForeignKey('authrole.Role', related_name='users',
                             null=True, blank=True,
                             verbose_name=_('User role'))

    class Meta(object):
        abstract = True
