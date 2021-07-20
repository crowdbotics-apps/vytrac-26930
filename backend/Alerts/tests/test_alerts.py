import datetime

from icecream import ic
from rest_framework import status

from Alerts.models import Alert
from Functions.TestClass import TestClass
from calendars.models import DateType, Event
from Functions.calendar_setup import calendar_setup


class WebsocketTests(TestClass):
    def setUp(self):
        super().setUp()

        self.url = f"alerts/?token={self.token}"
    # def _create_data(self):
    #     pass
    # def _create_events(self):
    #     pass
    # def tearDown(self):
    # destroy_data
    # TODO


class AlertsTests(TestClass):
    def setUp(self):
        super().setUp()

        # obj1 = Event.objects.create(date_type=self.date1, created_by=self.user)
        # obj1.users.set([self.user])
        # obj1.save()
        #
        # obj2 = Event.objects.create(date_type=self.date2, created_by=self.user)
        # obj2.users.set([self.user3])
        # obj2.save()
        #
        # obj3 = Event.objects.create(date_type=self.date2, created_by=self.user)
        # obj3.users.set([self.user, self.user3])
        # obj3.save()
        # self.all_dates = Event.objects.all().count()

    # if request(f'ws://localhost:8000/alerts/?token={self.token}&x=xxx'):
    #     self.fail('server is not runing')

    def test_dates_notifcations(self):

        res = self.client.post('/calendars/', {
            "title": "first",
            "description": "",
            "start": self.after_1_d,
            "end": self.after_3_d,
            "from_time": self.after_1_h,
            "to_time": self.after_5_h,
            "created_by": 1,
            "date_type": 1,
            "users": [1],
            "recurrence": [
            ],
        })
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        # TODO test target`
        # TODO test filter`ing
