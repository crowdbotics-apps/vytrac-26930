from icecream import ic
from rest_framework import status
from django.contrib.auth.models import Group

from Functions.TestClass import TestClass


class TestBasics(TestClass):
    def test__spsfic_fields_permission(self):
        res = self.client.get('/groups/all_permissions/')
        self.assertEqual(res.status_code,status.HTTP_200_OK)

    def test_add_grooup(self):
        params = {
            "name": 'docktor',
            "permissions": [1, 2]
        }
        res = self.client.post('/groups/',params)
        self.assertEqual(res.status_code,status.HTTP_201_CREATED)
        self.assertEqual(Group.objects.last().permissions.count(),2)

