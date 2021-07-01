from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from Functions.TestClass import TestClass
from users.models import User
from users.utils import Util

class AuthTestings(TestClass):

    def test_verfy_email(self):
        res = self.client.post('/users/register/', {
            "email": 'fake@g.com',
            "username": 'mynewusername',
            "password": 'password',
        })

        self.assertEqual(res.status_code,status.HTTP_201_CREATED)
        user = User.objects.get(email='fake@g.com')

        self.assertFalse(user.is_email_verified)
        token = RefreshToken.for_user(user).access_token
        token = str(token)
        res = self.client.get(f'/users/verify_email/?token={token}')
        user = User.objects.get(email='fake@g.com')
        self.assertTrue(user.is_email_verified)
    #
    def test_sending_email(self):
        data = {'email_body': 'email_body', 'to_email': 'weplutus@gmail.com','email_subject': 'Reset your password.'}
        Util.send_email(data)

    # def test_verfy_email2(self):
    # TODO
    # email = requests.get('http://emailsgernator.com')
    #     res = self.client.post('/users/register/', {
    #         "email": email.adress,
    #         "username": 'mynewusername',
    #         "password": 'password',
    #     })
    #
    #     self.assertEqual(res.status_code, status.HTTP_201_CREATED)
    #     token = email.inbox.body.toekn
    #     res = self.client.get(f'/users/verify_email/?token={token}')
    #     user = User.objects.get(email='fake@g.com')
    #     self.assertTrue(user.is_email_verified)
