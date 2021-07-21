from unittest.mock import patch

import celery
from django.core.management import call_command
from django.test import TestCase, override_settings, SimpleTestCase
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from icecream import ic
from rest_framework.test import APITestCase, APISimpleTestCase

from Alerts.models import Alert
from Alerts.tasks import create_alert, add
from celery.contrib.testing.worker import start_worker

from users.models import Note
from vytrac_26930.celery import app


class AddTestCase(SimpleTestCase):
    allow_database_queries = True
    databases = '__all__'

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.celery_worker = start_worker(app)
        cls.celery_worker.__enter__()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.celery_worker.__exit__(None, None, None)

    def test_add(self):
        result = add.delay(8, 8)
        assert result.get() == 16
        assert result.successful() == True

    def test_note_alert_date(self):
        new_note = Note.objects.create(title='my title',description='my desc',alert_date='')

    def test_create_alert(self):
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=10,
            period=IntervalSchedule.SECONDS, )

        PeriodicTask.objects.create(
            interval=schedule,
            name='Importing contacts',
            task='proj.tasks.import_contacts',
            one_off=True
            # args=[]
            # kwargs={}
        )
        perams = {
            "object_id": 3,
            "messages": {'messages': 'rexx'}
        }

        result = create_alert.delay(1, perams)
        # TODO create alert for note alert_date
