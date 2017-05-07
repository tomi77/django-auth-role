from __future__ import unicode_literals

from django.contrib.auth.backends import ModelBackend


class BaseAuthRoleBackend(ModelBackend):
    """
    Authenticates against authrole.models.Role.
    """
    def fetch_role_permissions(self, user_obj):
        raise NotImplementedError()

    def get_role_permissions(self, user_obj, obj=None):
        """
        Returns a set of permission strings that this user has through his/her
        role.
        """
        if user_obj.is_superuser:
            return set()
        if not hasattr(user_obj, '_role_perm_cache'):
            perms = self.fetch_role_permissions(user_obj) \
                .values_list('content_type__app_label', 'codename') \
                .order_by()
            user_obj._role_perm_cache = set(['%s.%s' % (ct, name)
                                             for ct, name in perms])
        return user_obj._role_perm_cache

    def get_all_permissions(self, user_obj, obj=None):
        if user_obj.is_anonymous() or obj is not None:
            return set()
        user_obj._perm_cache = super(BaseAuthRoleBackend, self) \
            .get_all_permissions(user_obj, obj)
        user_obj._perm_cache.update(self.get_role_permissions(user_obj))
        return user_obj._perm_cache
