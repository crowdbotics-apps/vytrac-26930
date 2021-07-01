from django.contrib.auth.models import Group
from icecream import ic

from Functions.make_fields_permissions import make_fields_permissions

from rest_framework import status

from Alerts.models import Alert, AlertRule
from Functions.TestClass import TestClass
from calendars.models import Event
from Functions.calendar_setup import calendar_setup
from patients.models.models import Patient

class TestRules(TestClass):
    def setUp(self):
        super().setUp()
        calendar_setup(self)
        Group.objects.create(name='patients')
        Group.objects.create(name='providers')
        from django.contrib.auth.models import Permission
        from django import apps
        from Alerts.models import AllDataStr
        from django.contrib.contenttypes.models import ContentType
        for Model in apps.apps.get_models():
            try:
                make_fields_permissions(Permission, ContentType, Model)
            except:
                pass
        for i in Permission.objects.all():
            if 'Can view' not in i.name:
                i.name = i.name.replace('Can ', '')
                newdata, created = AllDataStr.objects.get_or_create(name=i.name, codename=i.codename)
                newdata.content_type = i.content_type
                newdata.save()

    def test_monitor(self):
        i = Alert.objects.all().count()
        event = Event.objects.create(created_by=self.user, title='event')
        f = Alert.objects.all().count()
        assert f == i + 1


    def test_monitor_delete(self):
        i = Alert.objects.all().count()
        event = Event.objects.create(created_by=self.user, title='event')
        event.delete()
        f = Alert.objects.all().count()
        # assert f == i + 2 #TODO Note you may not need alerts for deleting events, only incase the event deadline not passed yet

    def test_adding_users(self):
        i = Alert.objects.all().count()
        data = {
            "title": "first",
            "description": "",
            "start": self.after_1_d,
            "end": self.after_3_d,
            "from_time": self.after_1_h,
            "to_time": self.after_5_h,
            "created_by": 1,
            "date_type": 1,
            "users": [self.user.id,self.user2.id],
            "recurrence": [
            ],
        }
        res = self.client.post('/calendars/', data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        f = Alert.objects.all().count()
        new_alert = Alert.objects.latest()
        assert new_alert.users.count() == 2
        assert f == i + 1

    def test_dont_monitor(self):
        i = Alert.objects.all().count()
        patient = Patient.objects.create(user=self.user)
        f = Alert.objects.all().count()
        assert f == i

    def test_rule_typos(self):
        params = {
            "trigers": ['add patent'],
            "users": [self.user.id, self.user2.id],
        }
        res = self.client.post('/alerts/rules/', params)
        # TODO add did you mean
        assert f"You may have a typo in the triger name add patent" in str(res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_rule(self):
        data = {
            "trigers": ['add patient'],
            "users": [self.user.id, self.user2.id],
        }
        assert AlertRule.objects.count() == 0
        res = self.client.post('/alerts/rules/', data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        assert res.data['users'] == [1, 2]
        ic(res.data)
        assert AlertRule.objects.count() == 1

        i = Alert.objects.all().count()
        Patient.objects.create(user=self.user)
        f = Alert.objects.all().count()
        assert f == i + 1

    def test_rule_invalid_data(self):
        data = {
            "tigers": ['add patient'],
            "users":[{'x':'d'}],
        }
        res = self.client.post('/alerts/rules/', data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_groups(self):
        data = {
            "tigers": ['add patient'],
            "groups":['patients','providers'],
        }
        assert AlertRule.objects.count() == 0
        res = self.client.post('/alerts/rules/', data)
        assert res.data['groups'] == [1, 2]
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        assert AlertRule.objects.count() == 1

    def test_groups_typo(self):
        data = {
            "tigers": ['add patient'],
            "groups":['patients','prov'],
        }
        res = self.client.post('/alerts/rules/', data)
        assert "You may have a typo in the group name prov" in str(res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)


    def test_watch_notes_alerts(self):
        data = {
            "tigers": ['add patient'],
            "users": [{'x': 'd'}],
        }
        res = self.client.post('/alerts/rules/', data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

        # i = Alert.objects.all().count()
        # patient = Patient.objects.create(user=self.user)
        # f = Alert.objects.all().count()
        # assert f == i+1

            # def test_monitor_spsfic_field(self):
    #     res = self.client.put('/alerts/rules/1/', {
    #         "field_value": 'name',
    #     })
    #
    #     event = Event.objects.create(created_by=self.user, title='event')
    #     f = Alerts.objects.all().latest()
    #     ic(f)
    #     assert f == initial + 1 #TODO
    #
    # def test_alert_only_target_users_groups(self):
    #     res = self.client.post('/alerts/rules/', {
    #         "users": [1],
    #         "groups": [1,3],
    #     })
    #
    #     event = Event.objects.create(created_by=self.user, title='event')
    #     f = Alerts.objects.all().latest()
    #     ic(f)
    #     assert f == initial + 1 #TODO
