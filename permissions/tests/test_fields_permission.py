import datetime

from django.contrib.auth.models import Group
from faker import Faker

from Functions.Permissions import perm
from Functions.TestClass import TestClass
from Functions.make_fields_permissions import make_fields_permissions
from calendars.models import DateType
from patients.models import Patient
from users.models import User

fake = Faker()
import django
django.setup()


class FieldsPerms(TestClass):
    def setUp(self):
        super().setUp()

        from django.contrib.auth.models import Permission
        from django import apps
        from django.contrib.contenttypes.models import ContentType
        for Model in apps.apps.get_models():
            try:
                make_fields_permissions(Permission, ContentType, Model)
            except:
                pass


        Patient.objects.create(user=self.user)
        Patient.objects.create(user=self.user2)
        Patient.objects.create(user=self.user3)

        group = Group.objects.create(name='provider')
        group.permissions.add(perm('Can view user', User))
        group.save()
        #
        enconter = Group.objects.create(name='enconter')
        enconter.permissions.add(perm('Can view username', User))
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
        date_format = '%Y-%m-%d'
        time_format = '%H:%M:%S'
        d = datetime.datetime
        self.now = d.now().strftime(time_format)
        after_1_h = d.now() + datetime.timedelta(hours=1)
        after_5_h = d.now() + datetime.timedelta(hours=5)
        #
        after_1_d = d.now() + datetime.timedelta(days=1)
        after_3_d = d.now() + datetime.timedelta(days=3)
        #
        self.after_1_h = after_1_h.strftime(time_format)
        self.after_5_h = after_5_h.strftime(time_format)
        self.after_1_d = after_1_d.strftime(date_format)
        self.after_3_d = after_3_d.strftime(date_format)
        DateType.objects.create(name='meeting')
        #
        self.user.is_staff = False
        self.user.is_superuser = False
        self.user.save()


    def test_basic(self):
        username_perm = perm('Can view username', User)
        # assert username_perm #TODO
        user = self.user
        user.user_permissions.add(perm('Can view username', User))
        user.save()
        res = self.client.get('/users/')
        # ic(res.data) #TODO

    def test__spsfic_fields_permission(self):
        res = self.client.get('/users/')
        # self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        assert self.user.user_permissions.all().count() == 0

        user = self.user
        user.user_permissions.add(perm('Can view email', User))
        user.save()

        # assert self.user.user_permissions.count() == 1

        res = self.client.get('/users/')
        # ic(res.data)
        # self.assertEqual(res.status_code, status.HTTP_200_OK)
        # assert 'email' in res.data[0]
        # assert 'username' not in res.data[0]

