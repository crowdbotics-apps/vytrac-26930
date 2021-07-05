from datetime import datetime

from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from icecream import ic
from rest_framework import serializers
from safedelete.signals import pre_softdelete


def baseic_pre_save(sender, instance, *args, **kwargs):
    from django.apps import apps
    model_name = sender.__name__
    messages = {}
    id = instance.id
    Model = apps.get_model(instance._meta.app_label, model_name)

    @receiver(pre_softdelete, sender=Model)
    def pre_soft_del(instance, **kwargs):
        ic('pre_soft_del')
        id = None


    @receiver(m2m_changed, sender=Model.users.through)
    def m2m_change(**kwargs):
        pass
        # ic(kwargs)


    class DateSer(serializers.ModelSerializer):
        class Meta:
            model = sender
            fields = '__all__'



    if id:
        obj = Model.objects.get(id=instance.id)
        new_data = DateSer(obj, many=False).data
        old_data = DateSer(instance, many=False).data

        for key in old_data.keys():
            if not old_data[key] and not new_data[key]:
                new_data[key] = old_data[key]

            if new_data[key] == old_data[key]:
                new_data.pop(key) if key != 'id' else None

        if (len(new_data) > 1) and ('deleted' not in new_data):
            messages['new data'] = new_data

        # TODO add recurence
        # ic(new_data['recurrence'])
        create_alert(sender, instance, messages, instance.users.all())

def baseic_post_save(sender, created, instance, update_fields, **kwargs):
    messages = {}
    if created:
        messages['type'] = "created"

    create_alert(sender, instance, messages, instance.users.all())


def create_alert(sender, instance, messages, users=None, groups=None):
    from Alerts.models import Alert
    content_type = ContentType.objects.get_for_model(sender)
    if len(messages) > 0:
        new_alert = Alert.objects.create(object_id=instance.id, content_type=content_type, messages=messages)
        if users:
            new_alert.users.set(users)
        if groups:
            new_alert.groups.set(groups)
        new_alert.save()

def baseic_pre_soft_delete(sender, instance, *args, **kwargs):

    messages = {}
    messages['type'] = "soft delete"
    to_time = instance.to_time
    end = instance.end
    is_passed_day = False
    is_passed_hours = False

    if to_time:
        to_time = datetime.strptime(to_time, '%H:%M:%S')
        is_passed_hours = to_time <= datetime.now()

    if end:
        end = datetime.strptime(end, '%Y-%m-%d')
        is_passed_day = end <= datetime.now()
        is_passed_hours = True if (instance.to_time == None) else is_passed_hours

    if not (is_passed_day and is_passed_hours):
        create_alert(sender, instance, messages, instance.users.all())


def baseic_m2m(sender,action, instance, *args, **kwargs):
    from Alerts.models import Alert
    content_type = ContentType.objects.get_for_model(sender)
    alert = Alert.objects.filter(object_id=instance.id, content_type__model='event',content_type__app_label=content_type.app_label).first()
    alert.users.set(instance.users.all())
    alert.save()