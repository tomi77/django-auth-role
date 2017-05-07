from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AuthRoleConfig(AppConfig):
    name = 'authrole'
    verbose_name = _("User Roles")
