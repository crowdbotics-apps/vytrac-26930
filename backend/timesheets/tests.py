import datetime
from unittest import mock

import pytz
from rest_framework import status

from Functions.TestClass import TestClass
from Functions.calendar_setup import calendar_setup
from timesheets.models import Column, Value


def is_odd(num):
    return (num % 2) != 0


class TestTimeSheets(TestClass):

    def setUp(self, **kwargs):
        super().setUp()


        cal1 = Column.objects.create(name='oxygen', user=self.user)

        cal2 = Column.objects.create(name='blood_pressure', user=self.user)

        cal3 = Column.objects.create(name='is_seen', user=self.user)

        for i in range(4):
            Value.objects.create(object_id=1, column=cal1, field_value=i)

        for i in range(1,5):
            mocked = datetime.datetime(2018, 4, i, 0, 0, 0, tzinfo=pytz.utc)
            with mock.patch('django.utils.timezone.now', mock.Mock(return_value=mocked)):
                object_id = i if is_odd(i) else i - 1
                Value.objects.create(object_id=object_id, column=cal2, field_value=str(i + 1))


        for i in range(1, 7):
            mocked = datetime.datetime(2018, 4, i, 0, 0, 0, tzinfo=pytz.utc)
            with mock.patch('django.utils.timezone.now', mock.Mock(return_value=mocked)):
                object_id = i if is_odd(i) else i-1
                Value.objects.create(object_id=object_id, column=cal3, field_value=str(not is_odd(i)))

    def test_statistics_url(self):
        res = self.client.get('/statistics/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_statistics_url_post(self):
        res = self.client.post('/statistics/',
                               {
                                   "field_value": "22",
                                   "name": "ccc",
                                   'object_id':'1',
                                   "action": "added",
                                   "seen_by": [self.user.id],
                                   "date_created": "2021-06-09T10:42:41.458057Z",
                                   "column": {
                                       "name": "xx",
                                       "user": self.user.id
                                   }
                               }
                               )
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_typos(self):

        data = {
            "field_value": "22",
            "name": "ccc",
            "action": "added",
            "seen_by": [self.user.id],
            "date_created": "2021-06-09T10:42:41.458057Z",
            "column": {
                "name": "oxgyn",
                "user": 1
            }
        }
        res = self.client.post('/statistics/', data)

        assert "Did you mean ['oxygen']?" in str(res.data)
        self.assertNotEqual(res.status_code, status.HTTP_201_CREATED)

        data['sure'] = "true"
        res = self.client.post('/statistics/', data)
        # self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    # def test_is_seenst_earliest(self):
    #     res = self.client.get('/statistics/?is_seenst=true')
    #     # assert res.data[0]['column']['name'] == 'blood_pressure'
    #
    #     res = self.client.get('/statistics/?earliest=true')
    #     assert res.data[0]['column']['name'] == 'is_seen'

    def test_mutli_quries(self):
        res = self.client.get('/statistics/?earliest=true&fields=field_value,date_created')
        assert 'seen_by' not in str(res.data)
        assert 'field_value' in str(res.data)

    def test_depth_qures(self):
        res = self.client.get('/statistics/?column__name=oxygen')
        for i in res.data:
            assert i['column']['name'] == 'oxygen'

        res = self.client.get('/statistics/?column__name=is_seen')
        for i in res.data:
            assert i['column']['name'] == 'is_seen'

    def test_statstics_basic(self):
        res = self.client.get('/statistics/?cal=sum&resample=2D&column__name=blood_pressure')
        # Debugging(res.data, color='green')

    def test_statstics_duration(self):
        """
        How long the oxgyn took to change fro 80 to 90
        """
        res = self.client.get('/statistics/?cal=duration&column__name=oxgyen&column__user=1&intial=80&final=90')
        # assert 'days' in str(res.data['1']) #TODO

