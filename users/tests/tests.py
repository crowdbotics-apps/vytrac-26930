from icecream import ic
from rest_auth.tests.mixins import APIClient
from rest_framework import status
from rest_framework.test import APITestCase

from Functions.TestClass import TestClass
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'crowboticstest@gmail.com'
# EMAIL_HOST_PASSWORD = 'crowbotics123@1'
from timesheets.models import Column, Value
from users.models import User


class AuthTestings(TestClass):

    def test_get_statstics(self):
        col = Column.objects.create(name='Oxygen', user=self.user)
        Value.objects.create(object_id='1', field_value='96%', column=col)
        Value.objects.create(object_id='2', column=col)
        res = self.client.get('/users/')
        for i in res.data:
            if i['username'] == self.user.username:
                assert i['statistics'][0]['name'] == 'Oxygen'
                assert i['statistics'][0]['values'][0]['object_id'] == '1'
                assert i['statistics'][0]['values'][0]['field_value'] == '96%'

    # def test_get_patients(self):
    #     res = self.client.get('/users/?groups__containse=patient', data={'format': 'json'})
    #     self.register_data['email'] = api.rondomeemail
    #     resonse = self.client.post('users/register/', self.register_data, format='json')
    #
    #     resonse = self.client.post('users/verify_email/', self.register_data, format='json')

    # def test_api_jwt_and_permissions_and_users(self):
    #     assert User.objects.count() == 0
    #     self.client.post(self.register_url, self.register_data, format='json')
    #     assert User.objects.count() == 1
    #     u = User.objects.get(id=1)
    #     u.is_active = False
    #     u.save()
    #     #
    #     res = self.client.post(
    #         self.login_url, self.login_data, format='json')
    #     self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
    #     #
    #     u.is_active = True
    #     u.is_email_verified = True
    #     u.is_role_verified = True
    #     u.save()
    #     #
    #     client = APIClient()
    #     res = client.post(
    #         self.login_url, self.login_data, format='json')
    #     self.assertEqual(res.status_code, status.HTTP_200_OK)
    #     self.assertTrue('access' in res.data)
    #     token = res.data['access']
    #     refresh_token = res.data['refresh']
    #     #
    #     verification_url = '/users/token/verify/'
    #     res = self.client.post(
    #         verification_url, {'token': token}, format='json')
    #     self.assertEqual(res.status_code, status.HTTP_200_OK)
    #     #
    #     res = self.client.post(
    #         verification_url, {'token': 'abc'}, format='json')
    #     self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
    #     #
    def test_is_owner(self):
        self.user.is_superuser = False
        self.user.is_staff = False
        self.user.save()
        #
        res = self.client.get('/users/')
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        assert 'You are not permitted to view user' in str(res.data['permission error'])
        #
        res = self.client.get('/users/1/')
        assert self.user.id == 1
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_address(self):
        res = self.client.get('/users/address')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_availablity(self):
        res = self.client.get('/users/availablity')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_notes(self):
        res = self.client.get('/users/notes')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_nnn(self):
        res = self.client.get('/users/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
