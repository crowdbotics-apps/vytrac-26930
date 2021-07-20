from icecream import ic
from rest_framework import status

from Functions.TestClass import TestClass
from calendars.models import Event


class TrashTests(TestClass):
    def test_delete_event(self):
        event = Event.objects.create(created_by=self.user, title='event')
        res = self.client.get('/archive/')
        assert len(res.data) == 0

        res = self.client.delete('/calendars/1/')
        res = self.client.get('/archive/')
        assert len(res.data) == 1

    def test_retrieve(self):
        event = Event.objects.create(created_by=self.user, title='event')
        res = self.client.get('/calendars/')
        assert len(res.data) == 1

        res = self.client.delete('/calendars/1/')

        res = self.client.get('/calendars/')
        assert len(res.data) == 0

        # new item is achived
        res = self.client.get('/archive/')
        assert len(res.data) == 1

        # retrieve the item
        res = self.client.post('/archive/calendars/Event/1/')

        res = self.client.get('/calendars/')
        assert len(res.data) == 1

        #arvhive is empty now
        res = self.client.get('/archive/')
        assert len(res.data) == 0


    def test_delete_for_ever(self):
        event = Event.objects.create(created_by=self.user, title='event')
        assert Event.objects.all_with_deleted().count() ==1
        res = self.client.get('/calendars/')
        assert len(res.data) == 1

        res = self.client.delete('/calendars/1/')
        res = self.client.delete('/archive/calendars/Event/1/')

        assert Event.objects.all_with_deleted().count() == 0


    def test_undelete_message(self):
        event = Event.objects.create(created_by=self.user, title='event')
        res = self.client.delete('/calendars/1/')
        res = self.client.post('/archive/calendars/Event/33/')
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

        res = self.client.post('/archive/calendars/Event/1/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)