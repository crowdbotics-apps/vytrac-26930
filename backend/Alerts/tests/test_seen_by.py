from rest_framework import status
from rest_framework.test import APITestCase


from Functions.TestClass import TestClass


class SennBytests(TestClass):

    def test_basic(self):
        res = self.client.get('/alerts/seen_by/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)