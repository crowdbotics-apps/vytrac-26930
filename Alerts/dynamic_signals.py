from django.contrib.contenttypes.models import ContentType
from django.dispatch import receiver
from icecream import ic
from rest_framework import serializers
from safedelete.signals import pre_softdelete


def dynamic_alert(sender, instance, **kwargs):
    from django.apps import apps
    from Alerts.models import AlertRule
    from Alerts.signals import create_alert
    if sender.__name__ not in ['AlertRule', 'AllDataStr', 'Permission', 'OutstandingToken', 'Migration']:

        model_name = sender.__name__
        messages = {}
        try:
            id = instance.id
        except:
            id = None

        Model = apps.get_model(instance._meta.app_label, model_name)
        is_soft_del = False
        created = not id

        @receiver(pre_softdelete, sender=sender)
        def pre_soft_del(**kwargs):
            is_soft_del = True


        for rule in AlertRule.objects.all():
            for i in rule.trigers.all():
                model = i.content_type.model
                content_type = i.content_type
                if ContentType.objects.get_for_model(sender) == content_type:
                    created = ('add' in i.codename) and created
                    if created:
                        messages['type'] = 'created'
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
    messages = {}
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