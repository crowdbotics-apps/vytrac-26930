from __future__ import absolute_import, unicode_literals
from celery import shared_task

@shared_task
def make_alerts(x,y):
    # TODO
    # for note in Note.objects.all():
    #     if note.alert_date == now:
    #         messages = []
    #         create_alert(Note, note, messages, [note.user])
    return x+y
