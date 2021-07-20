from __future__ import absolute_import, unicode_literals
import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangotests_28782.settings')

app = Celery('proj')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


app.conf.beat_schedule = {
    'add-every-2-seconds': {
        'task': 'tasks.add',
        'schedule': 2.0,
        'args': (16, 16)
    },
}


@app.task
def add(x, y):
    return x + y

@app.task(name='celery.ping')
def ping():
    # type: () -> str
    """Simple task that just returns 'pong'."""
    return 'pong'
