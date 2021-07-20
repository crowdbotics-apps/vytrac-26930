from icecream import ic
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from Functions.TestClass import TestClass
from users.models import User
from users.utils import Util


class AuthTestings(TestClass):

    def test_create_user(self):
        res = self.client.post('/users/', {
            "email": 'fake@g.com',
            "username": 'mynewusername',
            "password": 'Password123-',
        })
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_password_validator_at_lest_8_cha(self):
        res = self.client.post('/users/', {
            "email": 'fake@g.com',
            "username": 'mynewusername',
            "password": 'passwor',
        })
        assert 'Password must contain at least 8 characters.' in str(res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_validator_similarity(self):
        res = self.client.post('/users/', {
            "email": 'fake@g.com',
            "username": 'username123',
            "password": 'username456',
        })
        assert 'Password is too similar to the username' in str(res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_validator_special_char(self):
        res = self.client.post('/users/', {
            "email": 'fake@g.com',
            "username": 'username123',
            "password": 'StrongerPassword123',
        })
        assert 'Password must contain at least one special character.' in str(res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_verfy_email(self):
        res = self.client.post('/users/', {
            "email": 'fake@g.com',
            "username": 'mynewusername',
            "password": 'Password!-1',
        })

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = User.objects.get(email='fake@g.com')

        self.assertFalse(user.is_email_verified)
        token = RefreshToken.for_user(user).access_token
        token = str(token)
        res = self.client.get(f'/users/verify_email/?token={token}')
        user = User.objects.get(email='fake@g.com')
        self.assertTrue(user.is_email_verified)

    #
    def test_sending_email(self):
        data = {'email_body': 'email_body', 'to_email': 'weplutus@gmail.com', 'email_subject': 'Reset your password.'}
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
