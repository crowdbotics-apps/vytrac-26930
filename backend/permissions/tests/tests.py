import datetime

from django.contrib.auth.models import Group
from faker import Faker
from icecream import ic
from rest_framework import status

from Functions.Permissions import perm
from Functions.TestClass import TestClass
from calendars.models import DateType
from patients.models import Patient
from users.models import User

fake = Faker()
import django

django.setup()


class AuthTestings(TestClass):
    def setUp(self):
        super().setUp()

        Patient.objects.create(user=self.user)
        Patient.objects.create(user=self.user2)
        Patient.objects.create(user=self.user3)

        group = Group.objects.create(name='provider')
        group.permissions.add(perm('Can view user', User))
        group.save()
        #
        enconter = Group.objects.create(name='enconter')
        enconter.permissions.add(perm('Can view user username', User))
        enconter.save()
        self.enconter = enconter
        #
        doctor = Group.objects.create(name='doctor')
        doctor.permissions.add(perm('Can change user', User))
        self.doctor = doctor
        #
        boss = Group.objects.create(name='boss')
        boss.permissions.add(perm('Can view patient', Patient))
        boss.save()
        #
        d = datetime.datetime
        DateType.objects.create(name='meeting')
        #
        self.user.is_staff = False
        self.user.is_superuser = False
        self.user.save()

    def test_permission(self):
        resp = self.client.get('/users/')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        #
        provider = Group.objects.get(name='provider')
        self.user.groups.add(provider)
        self.user.save()
        res = self.client.get('/users/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    #
    def test_boss_can_see_patient(self):
        provider = Group.objects.get(name='boss')
        self.user.groups.add(provider)
        self.user.save()
        res = self.client.get('/patient/')
        # Debugging(Group.objects.get(name='boss').permissions.all(), color='green')
        # TODO "permission error": ", You are not permitted to view patient"
        # self.assertEqual(res.status_code, status.HTTP_200_OK)

    #

    def test_if_can_change_then_can_view(self):
        # provider = Group.objects.get(name='doctor')
        # self.user.groups.add(provider)
        self.user.user_permissions.add(perm('Can view user', User))
        self.user.save()
        res = self.client.get('/users/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_can_not_view_other_users(self):
        resp = self.client.get('/users/2/')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_can_not_change(self):
        # 0. can't update
        res = self.client.put('/users/2/', {'username': 'updated', 'password': 'Password1234@', 'email': 'Alex@g.com'})
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

        # 1. add permission
        self.user.user_permissions.add(perm('Can change user', User))
        self.user.save()

        # 3. change
        userI = self.user2
        res = self.client.put('/users/2/', {'email': 'Alex@g.com'})
        userF = self.user2
        # 4. test
        self.assertEqual(userI.username, userF.username)
        self.assertEqual(userI.email, userF.email)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_can_change_email(self):
        self.user.is_superuser = True
        self.user.save()

        userI = self.client.get('/users/1/').data
        resp = self.client.put('/users/1/', {'email': 'newfakeemail@g.com'})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        userF = self.client.get('/users/1/').data
        self.assertNotEqual(userI['email'], userF['email'])

    def test_permission_to_put(self):
        self.user.user_permissions.clear()
        self.user.is_staff = False
        self.user.is_superuser = False
        self.user.save()
        resp = self.client.put('/users/2/', {'username': 'updated', 'password': 'Password1234@'})
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

        self.user.user_permissions.add(perm('Can change user', User))
        self.user.save()
        resp = self.client.put('/users/2/', {'username': 'updated', 'password': 'Password1234@'})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_can_change(self):
        resp = self.client.put('/users/2/', {'username': 'updated', 'password': 'Password1234@'})
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        #
        self.user.user_permissions.add(perm('Can change user', User))
        self.user.save()
        resp = self.client.put('/users/2/', {'username': 'updated', 'password': 'Password1234@', 'email': 'my@g.com'})
        assert resp.data['username'] == 'updated'
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_is_owner(self):
        self.user.user_permissions.clear()
        self.user.is_staff = False
        self.user.is_superuser = False
        self.user.save()
        res = self.client.get('/users/2/')
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

        res = self.client.get('/users/1/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_is_put(self):
        self.user.user_permissions.clear()
        self.user.is_staff = False
        self.user.is_superuser = False
        self.user.save()
        res = self.client.put('/users/2/', {})
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

        res = self.client.put('/users/1/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_cant_update_to_ununique(self):
        res = self.client.put('/users/1/', {'username': self.user2.username, 'password': 'password'})
        assert 'user with this username already exists' in str(res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    #TODO
    # this should return 400 instead of filer
    # django.db.utils.IntegrityError: UNIQUE constraint failed: users_user.username
    # def test_cant_add_not_unique(self):
    #     self.user.is_superuser = True
    #     self.user.save()
    #     res = self.client.post('/users/',
    #                            {'username': self.user2.username, 'password': 'password', 'email': 'email@x.com'})
    #     ic(res.status_code, status=status)
        # assert 'user with this username already exists' in str(res.data)
        # self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    # TODO def test_staff_cannot_update_their_role(self):
    #     self.user.is_staff = True
    #   self.user.save()
    #   resp = self.client.put('/users/1/', {'is_superuser': 'true'})
    # self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_can_view_relational_felds(self):
        data = {
            "title": "first",
            "description": "",
            "start": self.after_1_d,
            "end": self.after_3_d,
            "from_time": self.after_1_h,
            "to_time": self.after_5_h,
            "created_by": 1,
            "date_type": 1,
            "users": [self.user.id],
            "recurrence": [
            ],
        }

        res = self.client.post('/calendars/', data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.user.is_staff = True
        self.user.is_superuser = True
        self.user.save()
        res = self.client.post('/calendars/', data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
