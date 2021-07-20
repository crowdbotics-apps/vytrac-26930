from datetime import datetime

import pytz
from icecream import ic
from rest_framework import status, serializers

from Functions.TestClass import TestClass
from calendars.models import Event
from timesheets.models import Column, Value
from users.models import Note


class AuthTestings(TestClass):

    def test_timezone(self):
        from django.utils import timezone
        import pytz
        import datetime

        paris_tz = pytz.timezone("Asia/Baghdad")
        Baghdad = paris_tz.localize(datetime.datetime(2012, 3, 3, 1, 30))

        paris_tz = pytz.timezone("Europe/Paris")
        paris = paris_tz.localize(datetime.datetime(2012, 3, 3, 1, 30))

        paris2 = paris_tz.localize(datetime.datetime(2012, 4, 10, 1, 30))
        new_event = Event.objects.create(created_by=self.user, title='event', to_time=paris, end=paris)
        new_note1 = Note.objects.create(alert_date=paris)
        new_note2 = Note.objects.create(alert_date=paris2)
        new_note1 = Note.objects.create(alert_date=paris)

        class NoteSer(serializers.ModelSerializer):
            class Meta:
                model = Note
                fields = '__all__'

        print(NoteSer(Note.objects.all(), many=True).data)

    def test_input_timezone_aware(self):
        import pytz
        paris_tz = pytz.timezone("Europe/Paris")
        params = {
            "title": 'my title',
            "description": '',
            # "alert_date": '2021-07-16T14:33:46.000000+01:00',
            # "alert_date": '2021-07-16T14:33:46.000000Z',
            "alert_date": '2021-07-16T14:33:46.000000',
            # "alert_date": paris_tz.localize(datetime(2012, 3, 3, 1, 30)),
            "users": [1, 2],
        }
        res = self.client.post('/users/notes', params)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        # Test view timezone
        self.user.timezone = "Europe/Prague"
        self.user.save()
        res = self.client.get('/users/notes')
        assert res.data[0]['alert_date'] == '2021-07-16T13:33:46+02:00'
