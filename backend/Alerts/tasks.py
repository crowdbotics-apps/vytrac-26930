from __future__ import absolute_import, unicode_literals

import os

from icecream import ic

from Alerts.models import Alert

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')

from celery import Celery
from django_celery_beat.models import PeriodicTask

app = Celery('proj')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task
def add(x, y):
    return x + y


@app.task
def create_alert(beat_id, perams, *args, **kwargs):
    from users.models import Note
    from django.contrib.contenttypes.models import ContentType

    content_type = ContentType.objects.get_for_model(Note)
    new_alert = Alert.objects.create(**perams)
    new_alert.content_type = content_type
    new_alert.save()
    return None


@app.task
def update_alert(*args, **kwargs):
    pass
    # alert = Alert.objects.get()
    # alert
