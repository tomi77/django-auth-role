from django.contrib.auth.models import Permission
from django.test.testcases import TestCase

from authrole.auth.backends import BaseAuthRoleBackend


class MyBackend(BaseAuthRoleBackend):
    def fetch_permission(self, user_obj):
        return Permission.objects.filter(group__roles__myusers__user=user_obj)

backend = MyBackend()


class BackendTestCase(TestCase):
    fixtures = ['role']

    def test_1(self):
        user = backend.authenticate(None, 'user1', 'test')
        permissions = backend.get_all_permissions(user)
        self.assertSetEqual(permissions, set())

    def test_2(self):
        user = backend.authenticate(None, 'user2', 'test')
        permissions = backend.get_all_permissions(user)
        self.assertSetEqual(permissions, {
            'app.can_add_model1',
            'app.can_update_model1',
            'app.can_delete_model1',
            'app.can_add_model2',
            'app.can_update_model2',
            'app.can_delete_model2',
        })