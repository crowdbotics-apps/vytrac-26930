from icecream import ic
from rest_framework import status

from Functions.TestClass import TestClass
from Functions.calendar_setup import calendar_setup
from users.models import Availability
from calendars.models import Event

login_data = {'username': 'Clover',
              'password': 'password'}


class CalinderTests(TestClass):
    def setUp(self):
        super().setUp()
        availability2 = Availability.objects.create(title='office hours',
                                                   user=self.user2,
                                                    from_time=self.after_1_h,
                                                    to_time=self.after_5_h,
                                                   start=self.after_5_d,
                                                   end=self.after_9_d,
                                                   recurrence=['1 sunday', '1 monday', '1 tuesday'])

        availability1 = Availability.objects.create(title='office hours',
                                                   user=self.user,
                                                   from_time=self.after_1_h,
                                                   to_time=self.after_5_h,
                                                   start=self.after_5_d,
                                                   end=self.after_9_d,
                                                   recurrence=['1 sunday', '1 monday', '1 tuesday'])

        availability3 = Availability.objects.create(title='office hours',
                                                    user=self.user3,
                                                    from_time=self.after_1_h,
                                                    to_time=self.after_5_h,
                                                    start=self.after_5_d,
                                                    end=self.after_9_d,
                                                    recurrence=['1 sunday', '1 monday', '1 tuesday'])

    def test_can_not_create_old_date(self):
        resp = self.client.get('/calendars/', format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        resp = self.client.post('/calendars/', {
            "recurrence": [
                "1 wednesday",
                "1 tuesday",
                "1 thursday"
            ],
            "date_created": "2021-05-30 14:22:23.327335+00:00",
            "title": "",
            "description": "",
            "start": "2021-05-31",
            "end": "2021-06-02",
            "from_time": "20:20:00",
            "to_time": "20:20:00",
            "priority": "low",
            "date_type": 1,
            "created_by": 1,
            "users": [],
        })
        assert "You can't have a meeting start or end before today." in str(resp.data)

    def test_can_not_create_overlapping_dates(self):

        res = self.client.post('/calendars/', {
            "title": "first",
            "description": "",
            "start": self.after_6_d,
            "end": self.after_8_d,
            "from_time": self.after_1_h,
            "to_time": self.after_5_h,
            "created_by": 1,
            "date_type": 1,
            "users": [1],
            "recurrence": [
                "1 sunday",
            ],
        })
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

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
                "1 sunday",
                "1 monday",
            ],
        })
        assert 'overlap error' in str(res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

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
        assert 'overlap error' in str(res.data)
        assert 'title' or 'description' not in str(res.data['overlap error'])
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)


        old = Event.objects.all().count()
        res = self.client.post('/calendars/', {
            "title": "first",
            "description": "",
            "start": self.after_6_d,
            "end": self.after_8_d,
            "from_time": self.after_2_h,
            "to_time": self.after_4_h,
            "created_by": 1,
            "date_type": 1,
            "users": [1],
            "recurrence": [
                "1 monday",
            ],
        })
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        assert Event.objects.all().count() == old + 1

    def test_cant_meet_before_today(self):
        res = self.client.post('/calendars/', {
            "title": "first",
            'recurrence': [],
            'created_by': 1,
            'from_time': '00:01:0.0',
            'to_time': '00:02:0.0',
            "description": "",
            "start": '2021-01-28',
            "end": '2021-01-29',
            "date_type": 1,
            "users": [1]
        })
        assert "You can't have a meeting start or end before today." in str(
            res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_availability_no_overlap(self):
        params = {
            # "recurrence": ...,
            # "date_created": ...,
            "title": 'my new event',
            # "description": ...,
            "start": self.after_1_d,
            "end": self.after_3_d,
            "recurrence": [],
            "from_time": self.after_2_h,
            "to_time": self.after_3_h,
            # "is_archived": ...,
            # "priority": ...,
            "date_type": 1,
            # "created_by": ...,
            "users": [1,2]
            # "seen_by": ...,
        }
        res = self.client.post('/calendars/',params)
        self.assertEqual(res.status_code,status.HTTP_400_BAD_REQUEST)
        assert 'availabilities' in str(res.data)
        assert 'no overlap error' in str(res.data)

    def test_availability_overlap(self):
        params = {
            # "recurrence": ...,
            # "date_created": ...,
            "title": 'my new event',
            # "description": ...,
            "start": self.after_6_d,
            "end": self.after_8_d,
            "recurrence": [],
            "from_time": self.after_2_h,
            "to_time": self.after_3_h,
            # "is_archived": ...,
            # "priority": ...,
            "date_type": 1,
            # "created_by": ...,
            "users": [1,2]
            # "seen_by": ...,
        }
        res = self.client.post('/calendars/',params)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_delete_event(self):
        event = Event.objects.create(created_by=self.user, title='event')
        res = self.client.get('/calendars/')
        assert len(res.data) == 1
        res = self.client.delete('/calendars/1/')
        res = self.client.get('/calendars/')
        assert len(res.data) == 0

        # self.assertEqual(create_res.status_code, status.HTTP_201_CREATED)
        # assert len(Date.objects.all()) >= 1
        # new_date = Date.objects.create(title='near', start=after_1_h, end=after_5_h,
        #                                created_by=User.objects.get(id=1))
        # new_date2 = Date.objects.create(title='far', start=after_10_h, end=after_11_h,
        #                                 created_by=User.objects.get(id=1))
        # new_date0 = Date.objects.create(title='old', start='2021-01-28T10:30:50.884397Z', end='2021-01-28T13:30:50.884397Z',
        #                                 created_by=User.objects.get(id=1))
        # new_date.users.set([user, user2])
        # assert len(Date.objects.all()) == 4
        # assert len(Date.objects.filter(users__in=[user, user2])) == 3
        #
        # dates = Date.objects.all()
        #
        # assert len(dates) == 4
        # dates = dates.filter(start__gte=now, end__gte=now)
        # assert len(dates) == 3
        #
        # create_res = self.client.post('/calendars/', {
        #     "title": "this is ntersected",
        #     "description": "",
        #     "start": after_2_h,
        #     "end": after_3_h,
        #     "date_type": 1,
        #     "users": [1]
        # }, format='json')
        # assert 'overlap error' in str(create_res.data)
        # self.assertEqual(create_res.status_code, status.HTTP_400_BAD_REQUEST)
