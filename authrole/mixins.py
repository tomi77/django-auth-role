from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class RoleMixin(models.Model):
    """
    Mixin class to extend model with a role.
    """
    role = models.ForeignKey(
        getattr(settings, 'AUTHROLE_ROLE_MODEL', 'authrole.Role'),
        related_name='users', null=True, blank=True,
        verbose_name=_('User role')
    )

    class Meta(object):
        abstract = True
