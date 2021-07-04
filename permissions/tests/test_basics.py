from rest_framework import status

from Functions.TestClass import TestClass


class TestBasics(TestClass):
    def test__spsfic_fields_permission(self):
        res = self.client.get('/groups/all_permissions/')
        self.assertEqual(res.status_code,status.HTTP_200_OK)

