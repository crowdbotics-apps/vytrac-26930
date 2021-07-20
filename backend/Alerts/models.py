from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import Group
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.utils.translation import ugettext_lazy as _
from safedelete.models import SafeDeleteModel
from safedelete.models import SafeDeleteModel
from safedelete.signals import pre_softdelete

from Alerts.Functions.create_alert import create_alert2
from calendars.models import Event
from users.models import User

now = datetime.now()

PRIORITIES = (
    ('00_low', _('Low')),
    ('10_normal', _('Normal')),
    ('20_high', _('High')),
    ('30_critical', _('Critical')),
    ('40_blocker', _('Blocker'))
)


class SeenBy(SafeDeleteModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='alert_seen_by_user', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    # def duration(self):
    #     return self.date_created - now


from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


class AllDataStr(models.Model):
    name = models.CharField(max_length=999, blank=True, null=True)
    codename = models.CharField(max_length=999, blank=True, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING, null=True)


class AlertRule(SafeDeleteModel):
    triggers = models.ManyToManyField(AllDataStr, blank=True)
    object_id = models.PositiveIntegerField(blank=True, null=True,
                                            help_text='if this blanck I will moniter all objects')
    filters = models.JSONField(max_length=30, null=True, blank=True)

    field_value = models.CharField(max_length=999, null=True, blank=True,
                                   help_text='If field value equal/gte/contains... then I will alert you')
    users = models.ManyToManyField(User, related_name='rule_alert_target_users', blank=True)
    groups = models.ManyToManyField(Group, related_name='rule_alert_target_groups', blank=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    priority = models.CharField(
        max_length=20, choices=PRIORITIES, default='10_normal')


class Alert(SafeDeleteModel):
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    messages = models.JSONField(max_length=30, null=True, blank=True)
    deadline = models.DateTimeField(_("deadline"), null=True, blank=True)
    users = models.ManyToManyField(User, related_name='alert_target_users', blank=True)
    groups = models.ManyToManyField(Group, related_name='alert_target_groups', blank=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    priority = models.CharField(
        max_length=20, choices=PRIORITIES, default='10_normal')

    class Meta:
        get_latest_by = 'date_created'


class SeeAlert(SafeDeleteModel):
    alert = models.ForeignKey(Alert, on_delete=models.CASCADE, null=True)
    seen_by = models.ManyToManyField(SeenBy, related_name='alert_seen_by', blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


def post_save_func(sender, instance, **kwargs):
    create_alert2(sender, instance, 'post_save', kwargs)


def pre_save_func(sender, instance, **kwargs):
    create_alert2(sender, instance, 'pre_save', kwargs)


def pre_softdelete_func(sender, instance, **kwargs):
    create_alert2(sender, instance, 'pre_softdelete', kwargs)


post_save.connect(post_save_func)
pre_save.connect(pre_save_func)
pre_softdelete.connect(pre_softdelete_func)
