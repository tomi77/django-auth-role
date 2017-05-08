from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Role(models.Model):
    name = models.CharField(max_length=128, unique=True,
                            verbose_name=_('Role name'))
    groups = models.ManyToManyField('auth.Group', related_name='roles',
                                    verbose_name=_('Groups of permissions'))
    permissions = models.ManyToManyField('auth.Permission',
                                         related_name='roles',
                                         verbose_name=_('Permissions'))

    class Meta(object):
        verbose_name = _('Role')
        verbose_name_plural = _('Roles')

    def __repr__(self):
        return 'authrole.models.Role[pk=%d]' % self.pk

    def __str__(self):
        return self.name
