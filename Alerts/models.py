import re
from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import Group
from django.db import models
from django.db.models.signals import pre_save, m2m_changed, post_save, post_delete, pre_delete
from django.dispatch import receiver
from icecream import ic
from rest_framework import serializers
from safedelete.models import SafeDeleteModel
from safedelete.models import SafeDeleteModel
from django.utils.translation import ugettext_lazy as _
from calendars.models import Event
# from users.models import User, Note
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
    trigers = models.ManyToManyField(AllDataStr, blank=True)
    object_id = models.PositiveIntegerField(blank=True, null=True,
                                            help_text='if this blanck I will moniter all objects')
    filter = models.CharField(max_length=999, help_text='example: "oxgyn__lt=80"', blank=True, null=True)
    field_value = models.CharField(max_length=999, null=True, blank=True,
                                   help_text='If field value equal/gte/contains... then I will alert you')
    users = models.ManyToManyField(User, related_name='rule_alert_target_users', blank=True)
    groups = models.ManyToManyField(Group, related_name='rule_alert_target_groups', blank=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    priority = models.CharField(
         max_length=20, choices=PRIORITIES, default='10_normal')


class Alert(SafeDeleteModel):
    is_archived = models.BooleanField(default=False)
    #TODO if is archived filter out from view
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


def create_alert(sender, instance, messages,users=None,groups=None):
    content_type = ContentType.objects.get_for_model(sender)
    if len(messages) > 0:
        new_alert = Alert.objects.create(object_id=instance.id, content_type=content_type,messages=messages)
        if users:

            new_alert.users.set(None)
        if groups:
            new_alert.groups.set(groups)
        new_alert.save()





@receiver(post_save)
def dynamic_alert(sender, instance,created, **kwargs):



    if sender.__name__ not in ['AlertRule', 'AllDataStr', 'Permission','OutstandingToken','Migration']:

        messages = []

        for rule in AlertRule.objects.all():
            for i in rule.trigers.all():
                model = i.content_type.model
                content_type = i.content_type

                if ContentType.objects.get_for_model(sender) == content_type:
                    messages.append({'type':'created'}) if created else None
                    create_alert(sender, instance, messages)


    class MySer(serializers.ModelSerializer):
        class Meta:
            model = sender
            fields = '__all__'

    # if m2m:
    #     sender_name = re.findall(r"(.+?)_(.+)", sender.__name__)
    #     model_name = sender_name[0][0]
    #     field_name = sender_name[0][1]
    #     pass
    messages = []
    if kwargs.get('created'):

        messages.append({'created': 'true'})
        serializer = MySer(instance, many=False)
    else:
        # Model = apps.get_model(instance._meta.app_label, model_name)
        # Model = apps.get_model(instance._meta.app_label, sender.__name__)
        # obj = Model.objects.get(id=instance.id)
        # data = MySer(obj, many=False).data
        olddata = MySer(instance, many=False).data
        # for key in olddata.keys():
        # if data[key] == olddata[key]:
        #     data.pop(key) if key != 'id' else None
    # for alert in AlertsRules.objects.all():
    #
    #     serializer = MySer(instance, many=False)
    #     messages.append({'updated': 'true'})
    #
    #     messages.append({'model_name': sender.__name__})
    #     Alerts.objects.create(model=sender.__name__,messages=messages)





def baseic_post_save(sender, created, instance,update_fields, **kwargs):
    messages = []
    messages.append({'type': 'created'}) if created else None
    create_alert(sender, instance, messages,instance.users.all())


def baseic_post_delete(self,sender, instance, *args, **kwargs):
    messages = []
    messages.append({'type': 'delete'})
    create_alert(sender, instance,messages)

def baseic_m2m(sender, instance, *args, **kwargs):
    content_type = ContentType.objects.get_for_model(sender)
    alert = Alert.objects.filter(object_id=instance.id,content_type__model='event',content_type__app_label=content_type.app_label).first()
    alert.users.set(instance.users.all())
    alert.save()

basic_models = [Event]
for i in basic_models:
    post_save.connect(baseic_post_save, sender=i)
    m2m_changed.connect(baseic_m2m, sender=i.users.through)
    post_delete.connect(baseic_post_delete, sender=i)
    pre_delete.connect(baseic_post_delete, sender=i, dispatch_uid="delete_signal_dispatch")

