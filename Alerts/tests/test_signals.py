from django.contrib.auth.models import Group
from icecream import ic

from Functions.MyAppsConfig import create_all_data_str
from Functions.make_fields_permissions import make_fields_permissions

from rest_framework import status

from Alerts.models import Alert, AlertRule
from Functions.TestClass import TestClass
from calendars.models import Event
from Functions.calendar_setup import calendar_setup
from patients.models import Patient

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
        create_all_data_str(Permission,AllDataStr)

    def test_monitor(self):
        i = Alert.objects.all().count()
        event = Event.objects.create(created_by=self.user, title='event')
        f = Alert.objects.all().count()
        assert f == i + 1


    def test_dont_alert_delete_if_not_passed(self):
        i = Alert.objects.all().count()
        event = Event.objects.create(created_by=self.user, title='event',end=self.after_1_d)
        event.delete()
        f = Alert.objects.all().count()
        assert f == i+1

    def test_alert_if_passed(self):
        i = Alert.objects.all().count()
        event = Event.objects.create(created_by=self.user, title='event',end=self.before_1_d)
        event.delete()
        f = Alert.objects.all().count()
        messages = Alert.objects.latest().messages
        assert messages['type'] == 'soft delete'
        assert f == i + 2

    def test_pre_save_messages(self):
        i = Alert.objects.all().count()
        event = Event.objects.create(created_by=self.user, title='event',end=self.after_1_d)
        event.title = 'update'
        event.save()
        f = Alert.objects.all().count()
        ic(f,i)
        # TODO
        assert f == i + 2
        assert Alert.objects.latest().messages['new data']['title'] == 'event'


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
        ic(res.data)
        assert f"You may have a typo in the triger name add patent" in str(res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_rule(self):
        res = self.client.get('/alerts/trigers/?codename__contains=add_patient&content_type__model=patient')
        id = res.data[0]['id']
        assert res.data[0]['name'] == 'add patient'

        data = {
            "trigers": [id],
            "users": [self.user.id, self.user2.id],
        }
        assert AlertRule.objects.count() == 0
        res = self.client.post('/alerts/rules/', data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        assert res.data['users'] == [1, 2]
        assert AlertRule.objects.count() == 1

        i = Alert.objects.all().count()
        new_patient = Patient.objects.create(user=self.user)
        new_patient.score = 2
        new_patient.save() #this to test to not alert when updte and only when add

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
