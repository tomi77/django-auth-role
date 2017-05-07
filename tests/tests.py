import django
from django.contrib.auth.models import Permission, AnonymousUser
from django.test.testcases import TestCase

from authrole.auth.backends import BaseAuthRoleBackend


class MyBackend(BaseAuthRoleBackend):
    def fetch_role_permissions(self, user_obj):
        return Permission.objects.filter(group__roles__myusers__user=user_obj)


class MyBackendTestCase(TestCase):
    fixtures = ['role']

    backend = MyBackend()

    def test_empty_role(self):
        if django.VERSION[:2] < (1, 11):
            user = self.backend.authenticate('user1', 'test')
        else:
            user = self.backend.authenticate(None, 'user1', 'test')
        permissions = self.backend.get_all_permissions(user)
        self.assertSetEqual(permissions, set())

    def test_role(self):
        if django.VERSION[:2] < (1, 11):
            user = self.backend.authenticate('user2', 'test')
        else:
            user = self.backend.authenticate(None, 'user2', 'test')
        permissions = self.backend.get_all_permissions(user)
        self.assertSetEqual(permissions, {
            'app.can_add_model1',
            'app.can_update_model1',
            'app.can_delete_model1',
            'app.can_add_model2',
            'app.can_update_model2',
            'app.can_delete_model2',
        })

    def test_unauthorized(self):
        user = AnonymousUser()
        permissions = self.backend.get_all_permissions(user)
        self.assertSetEqual(permissions, set())

    def test_superuser(self):
        if django.VERSION[:2] < (1, 11):
            user = self.backend.authenticate('user3', 'test')
        else:
            user = self.backend.authenticate(None, 'user3', 'test')
        permissions = self.backend.get_all_permissions(user)
        all_permissions = Permission.objects.all().count()
        self.assertEqual(len(permissions), all_permissions)