import os

from icecream import ic

from Functions.MyAppsConfig import create_all_data_str
from Functions.calendar_setup import calendar_setup
from Functions.make_fields_permissions import make_fields_permissions

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangotests_28782.settings')

import django

django.setup()

from users.models import User
from rest_framework.test import APIClient, APITestCase
from rest_framework import status


class TestClass(APITestCase):
    def setUp(self):
        calendar_setup(self)

        from django.contrib.auth.models import Permission
        from django import apps
        from django.contrib.contenttypes.models import ContentType
        from Alerts.models import AllDataStr

        for Model in apps.apps.get_models():
            try:
                make_fields_permissions(Permission, ContentType, Model)
            except:
                pass
        try:

            create_all_data_str(Permission, AllDataStr)
        except:
            pass

        user, create = User.objects.get_or_create(username='Clover', email='Clover@g.com', password='password',
                                                  timezone='Asia/Baghdad')
        user.is_email_verified = True
        user.is_role_verified = True
        user.is_staff = True
        user.is_superuser = True
        user.save()

        user2, create2 = User.objects.get_or_create(date_joined='2021-05-28T13:30:50.884397Z', username='Alex',
                                                    email='Alex@g.com', password='password')
        user2.is_email_verified = True
        user2.is_staff = True
        user2.save()
        assert user2.is_superuser == False
        user.save()

        user3, create3 = User.objects.get_or_create(username='Sam', email='Sam@g.com', password='password',
                                                    is_email_verified=True)
        user3.is_email_verified = True
        user3.save()

        assert user3.is_staff == False
        assert user3.is_superuser == False

        for i in [create, create2, create3]:
            ic('=========== laready exist =========== ') if not i else None

        client = APIClient()
        lg_res = client.post('/users/login/', {'username': 'Clover', 'password': 'password'})
        lg_res2 = client.post('/users/login/', {'username': 'Alex', 'password': 'password'})
        lg_res3 = client.post('/users/login/', {'username': 'Sam', 'password': 'password'})
        token = lg_res.data["access"]
        token2 = lg_res2.data["access"]
        token3 = lg_res3.data["access"]
        res = client.get('/statistics/')
        assert res.status_code == status.HTTP_400_BAD_REQUEST

        client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        client = client

        res = client.get('/statistics/')
        assert res.status_code == status.HTTP_200_OK
        x = [user, user2, user3, token, token2, token3, client]
        self.user = user
        self.user2 = user2
        self.user3 = user3
        self.token = token
        self.token2 = token2
        self.token3 = token3
        self.client = client

    def test_TestClass_bais(self):
        assert self.user2.username
