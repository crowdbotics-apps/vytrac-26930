import datetime

from icecream import ic

from Alerts.models import Alert
from Functions.TestClass import TestClass
from calendars.models import DateType, Event


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


        date_format = '%Y-%m-%d'
        time_format = '%H:%M:%S'
        d = datetime.datetime
        self.now = d.now().strftime(time_format)
        after_1_h = d.now() + datetime.timedelta(hours=1)
        after_5_h = d.now() + datetime.timedelta(hours=5)
        self.after_1_h = after_1_h.strftime(time_format)
        self.after_5_h = after_5_h.strftime(time_format)

        after_2_h = d.now() + datetime.timedelta(hours=2)
        after_3_h = d.now() + datetime.timedelta(hours=3)
        self.after_2_h = after_2_h.strftime(time_format)
        self.after_3_h = after_3_h.strftime(time_format)

        after_10_h = d.now() + datetime.timedelta(hours=10)
        after_11_h = d.now() + datetime.timedelta(hours=11)
        self.after_10_h = after_10_h.strftime(time_format)
        self.after_11_h = after_11_h.strftime(time_format)

        after_1_d = d.now() + datetime.timedelta(days=1)
        after_3_d = d.now() + datetime.timedelta(days=3)

        self.after_1_d = after_1_d.strftime(date_format)
        self.after_3_d = after_3_d.strftime(date_format)
        self.date1 = DateType.objects.create(name='meeting')
        self.date2 = DateType.objects.create(name='appointment')

        obj1 = Event.objects.create(date_type=self.date1, created_by=self.user)
        obj1.users.set([self.user])
        obj1.save()

        obj2 = Event.objects.create(date_type=self.date2, created_by=self.user)
        obj2.users.set([self.user3])
        obj2.save()

        obj3 = Event.objects.create(date_type=self.date2, created_by=self.user)
        obj3.users.set([self.user, self.user3])
        obj3.save()
        self.all_dates = Event.objects.all().count()

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
        # self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        # #

        # TODO test target`
        # TODO test filter`ing
