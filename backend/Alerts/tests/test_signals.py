from django.contrib.auth.models import Group
from rest_framework import status

from Alerts.models import Alert, AlertRule
from Functions.TestClass import TestClass
from calendars.models import Event
from patients.models import Patient


class TestRules(TestClass):
    def setUp(self):
        super().setUp()
        Group.objects.create(name='patients')
        Group.objects.create(name='providers')
        res = self.client.get('/alerts/triggers/?codename__contains=add_patient&content_type__model=patient')
        id = res.data[0]['id']

        self.add_patient = id

        res = self.client.get('/alerts/triggers/?codename__contains=change_event&content_type__model=event')
        id = res.data[0]['id']

        self.change_event = id

    def test_monitor(self):
        i = Alert.objects.all().count()
        event = Event.objects.create(created_by=self.user, title='event')
        f = Alert.objects.all().count()
        # TODO add rule before
        # assert f == i + 1

    def test_alert_delete_if_not_passed(self):
        i = Alert.objects.all().count()
        event = Event.objects.create(created_by=self.user, title='event', end=self.after_1_d)
        event.delete()
        f = Alert.objects.all().count()
        # messages = Alert.objects.latest().messages
        # TODO
        # assert 'soft delete' in str(messages)
        # assert f == i + 2

    def test_dont_alert_if_passed(self):
        i = Alert.objects.all().count()
        event = Event.objects.create(created_by=self.user, title='event', end=self.before_1_d)
        event.delete()
        f = Alert.objects.all().count()
        # messages = Alert.objects.latest().messages
        # TODO
        # assert 'soft delete' not in str(messages)
        # assert f == i + 1

    def test_pre_save_messages_create(self):
        i = Alert.objects.all().count()
        event = Event.objects.create(created_by=self.user, title='event', end=self.after_1_d)
        event.title = 'update'
        event.save()
        f = Alert.objects.all().count()
        # TODO add rule
        # assert f == i + 2
        # TODO I should see update instead of event
        # assert Alert.objects.latest().messages['new data']['title'] == 'update'

    def test_m2m_changed(self):
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
            "users": [self.user.id, self.user2.id],
            "recurrence": []
        }
        res = self.client.post('/calendars/', data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        f = Alert.objects.all().count()
        # TODO

    def test_dont_monitor(self):
        i = Alert.objects.all().count()
        patient = Patient.objects.create(user=self.user)
        f = Alert.objects.all().count()
        assert f == i

    def test_add_rule(self):
        data = {
            "triggers": [self.add_patient],
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
        new_patient.save()

        f = Alert.objects.all().count()
        assert f == i + 1

    def test_rule_invalid_data(self):
        data = {
            "tigers": ['add patient'],
            "users": [{'x': 'd'}],
        }
        res = self.client.post('/alerts/rules/', data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_groups(self):
        data = {
            "triggers": [self.add_patient],
            "groups": ['patients', 'providers'],
        }
        assert AlertRule.objects.count() == 0
        res = self.client.post('/alerts/rules/', data)
        assert res.data['groups'] == [1, 2]
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        assert AlertRule.objects.count() == 1

    def test_filters(self):
        data = {
            "triggers": [self.add_patient],
            "groups": ['patients', 'providers'],
            "filters": {"score__gte": "9"},
        }
        res = self.client.post('/alerts/rules/', data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        #
        Patient.objects.create(user=self.user, score=12)
        Patient.objects.create(user=self.user2, score=7)
        Patient.objects.create(user=self.user3, score=12)
        assert Alert.objects.count() == 2

    def test_no_filters(self):
        data = {
            "triggers": [self.add_patient],
            "groups": ['patients', 'providers'],
        }
        res = self.client.post('/alerts/rules/', data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        #
        Patient.objects.create(user=self.user, score=12)
        Patient.objects.create(user=self.user2, score=7)
        Patient.objects.create(user=self.user3, score=12)
        assert Alert.objects.count() == 3

    def test_update_fields(self):
        data = {
            "triggers": [self.change_event],
            "groups": ['patients', 'providers'],
        }
        res = self.client.post('/alerts/rules/', data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        #
        new_event = Event.objects.create(created_by=self.user, title='event', end=self.after_1_d)
        new_event.title = 'new title'
        new_event.save()
        messages = Alert.objects.latest().messages
        assert messages['new data']['title'] == 'new title'
        assert messages['type'] == 'update'
        assert Alert.objects.count() == 1

    def test_update_m2m_fields(self):
        data = {
            "triggers": [self.change_event],
            "groups": ['patients', 'providers'],
        }
        res = self.client.post('/alerts/rules/', data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        #
        new_event = Event.objects.create(created_by=self.user, title='event', end=self.after_1_d)
        new_event.users.add(2)
        new_event.save()
        messages = Alert.objects.latest().messages
        # ic(messages)
        # TODO
        # assert messages['new data']['users'][0] == 2
        # assert messages['type'] == 'update'
        assert Alert.objects.count() == 1

        # def test_monitor_specific_field(self):
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

    # data = {
    #     "triggers": [self.add_event],
    #     "groups": ['patients', 'providers'],
    #     "filters": {"score__gte": "9"},
    # }
    # res = self.client.post('/alerts/rules/', data)
    #     res = self.client.post('/alerts/rules/', {
    #         "users": [1],
    #         "groups": [1,3],
    #     })
    #     initial = Alert.objects.count()
    #     event = Event.objects.create(created_by=self.user, title='event')
    #     f = Alert.objects.count()
    #     obj = Alert.objects.latest()
    #     ic(obj)
    #     assert f == initial + 1
