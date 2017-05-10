import django
from django.contrib.auth.models import Permission, AnonymousUser
from django.test.testcases import TestCase

from authrole.auth.backends import AuthRoleBackend


class AuthRoleBackendTestCase(TestCase):
    fixtures = ['role']

    backend = AuthRoleBackend()

    def authenticate(self, username, password):
        if django.VERSION[:2] < (1, 11):
            return self.backend.authenticate(username, password)
        else:
            return self.backend.authenticate(None, username, password)

    def test_anonymous_user(self):
        """Test anonymous user"""
        user = AnonymousUser()
        permissions = self.backend.get_all_permissions(user)
        self.assertSetEqual(permissions, set(),
                            msg='List of permissions should be empty')

    def test_superuser(self):
        """Test superuser"""
        user = self.authenticate('user3', 'test')
        permissions = self.backend.get_all_permissions(user)
        all_permissions = Permission.objects.all().count()
        self.assertEqual(len(permissions), all_permissions,
                         msg='List of permissions should have all permissions')

    def test_user_with_role_without_groups_and_permissions(self):
        """Test user without permissions and group of permissions and with role without permissions and group of permissions"""
        user = self.authenticate('user1', 'test')
        permissions = self.backend.get_all_permissions(user)
        self.assertSetEqual(permissions, set(),
                            msg='List of permissions should be empty')

    def test_user_with_role_with_groups_and_without_permissions(self):
        """Test user without permissions and group of permissions and with role without permissions and with group of permissions"""
        user = self.authenticate('user2', 'test')
        permissions = self.backend.get_all_permissions(user)
        self.assertSetEqual(permissions, {
            'app.can_add_model1',
            'app.can_update_model1',
            'app.can_delete_model1',
            'app.can_add_model2',
            'app.can_update_model2',
            'app.can_delete_model2',
        }, msg='List of permissions should should have all "app.can_*" '
               'permissions')

    def test_user_with_role_with_groups_and_permissions(self):
        """Test user without permissions and group of permissions and with role with permissions and group of permissions"""
        user = self.authenticate('user4', 'test')
        permissions = self.backend.get_all_permissions(user)
        self.assertSetEqual(permissions, {
            'app.can_add_model1',
            'app.can_update_model1',
            'app.can_delete_model1',
            'app.can_add_model2',
            'app.can_update_model2',
            'app.can_delete_model2',
            'app.some_operation_model2',
        }, msg='List of permissions should should have all "app.can_*" '
               'permissions and "app.some_operation_model2" permission')

    def test_user_with_role_without_groups_and_with_permissions(self):
        """Test user without permissions and group of permissions and with role with permissions and without group of permissions"""
        user = self.authenticate('user5', 'test')
        permissions = self.backend.get_all_permissions(user)
        self.assertSetEqual(permissions, {'app.some_operation_model2'},
                            msg='List of permissions should should have only '
                                '"app.some_operation_model2" permission')

    def test_user_without_role_and_permissions_and_groups(self):
        """Test user without permissions and group of permissions and role"""
        user = self.authenticate('user6', 'test')
        permissions = self.backend.get_all_permissions(user)
        self.assertSetEqual(permissions, set(),
                            msg='List of permissions should be empty')

    def test_user_without_role_and_groups_and_with_permissions(self):
        """Test user without role and group of permissions and with permissions"""
        user = self.authenticate('user7', 'test')
        permissions = self.backend.get_all_permissions(user)
        self.assertSetEqual(permissions, {'app.can_add_model1',
                                          'app.can_add_model2'},
                            msg='List of permissions should have all '
                                '"app.can_add_model*"')

    def test_user_without_role_and_permissions_and_with_group(self):
        """Test user without role and permissions and with group of permissions"""
        user = self.authenticate('user8', 'test')
        permissions = self.backend.get_all_permissions(user)
        self.assertSetEqual(permissions, {
            'app.can_add_model1',
            'app.can_update_model1',
            'app.can_delete_model1',
        }, msg='List of permissions should have all "app.can_add_model*"')

    def test_user_with_permission_and_role_without_groups_and_with_permissions(self):
        """Test user without group of permissions and with permissions and role without permissions and with group of permissions"""
        user = self.authenticate('user9', 'test')
        permissions = self.backend.get_all_permissions(user)
        self.assertSetEqual(permissions, {
            'app.can_add_model2',
            'app.can_update_model2',
            'app.can_delete_model2',
            'app.some_operation_model2',
        }, msg='List of permissions should should have all "app.*_model2" '
               'permission')

    def test_user_with_group_and_role_with_groups_and_without_permissions(self):
        """Test user without permissions and with group of permissions and role without permissions and with group of permissions"""
        user = self.authenticate('user10', 'test')
        permissions = self.backend.get_all_permissions(user)
        self.assertSetEqual(permissions, {
            'app.can_add_model1',
            'app.can_update_model1',
            'app.can_delete_model1',
            'app.can_add_model2',
            'app.can_update_model2',
            'app.can_delete_model2',
        }, msg='List of permissions should should have all "app.*_model1" and '
               '"app.*_model2" permission')
