from django.db.models.signals import m2m_changed
from icecream import ic

from Functions.queryset_filtering import queryset_filtering


def get_changed_fields(sender, instance, Model, messages):
    from rest_framework import serializers

    obj = Model.objects.filter(id=instance.id).first()

    class DateSer(serializers.ModelSerializer):
        class Meta:
            model = sender
            fields = '__all__'

    if obj:
        new_data = DateSer(instance, many=False).data
        old_data = DateSer(obj, many=False).data

        for key in old_data.keys():
            if not old_data[key] and not new_data[key]:
                new_data[key] = old_data[key]

            if new_data[key] == old_data[key]:
                new_data.pop(key)

            if (len(new_data) > 1) and ('deleted' not in new_data):
                messages['new data'] = new_data
                messages['type'] = 'update'

    messages['new data'] = new_data
    return []


# TODO handle users,groups in one of the following ways
def users_changed(sender, instance, action, **kwargs):
    if action == 'pre_add':
        ic('pre_add')

    if action == 'post_add':
        ic('post_add')
    ic(kwargs)
    ic(action)
    ic(instance.title)
    ic(instance.users.all())


def groups_changed(sender, instance, **kwargs):
    ic(instance.groups.all())


def users_changed(sender, instance, action, **kwargs):
    if action == 'pre_add':
        ic('pre_add')

    if action == 'post_add':
        ic('post_add')


def create_alert2(sender, instance, signal_type, kwargs):
    from Alerts.models import AlertRule, Alert
    from django.contrib.contenttypes.models import ContentType
    from django.apps import apps
    tag_user = None

    if sender.__name__ not in ['AlertRule', 'AllDataStr', 'Permission', 'OutstandingToken', 'Migration']:

        Model = apps.get_model(instance._meta.app_label, sender.__name__)

        try:
            m2m_changed.connect(users_changed, sender=Model.users.through)
        except:
            pass

        try:
            m2m_changed.connect(groups_changed, sender=Model.groups.through)
        except:
            pass

        content_type = ContentType.objects.get_for_model(sender)

        is_sender_match = None
        is_action_match = None

        try:
            is_tag_user = instance.user
        except:
            pass

        try:
            tag_users = instance.users.all()
        except:
            tag_users = None

        try:
            id = instance.id
        except:
            id = None

        created = kwargs.get('created')
        action = None
        if created:
            action = 'add'
        elif signal_type == 'pre_softdelete':
            action = 'delete'
        elif (signal_type == 'pre_save') and id:
            action = 'change'
        elif (signal_type == 'pre_save') and not id:
            action = 'pre_add'

        messages = {}

        for rule in AlertRule.objects.all():
            for i in rule.triggers.all():
                users = rule.users.all()
                groups = rule.groups.all()

                if rule.filters:
                    items = queryset_filtering(Model, rule.filters)
                else:
                    items = Model.objects.all()

                item = items.filter(id=instance.id)
                is_sender_match = i.content_type == content_type
                is_action_match = str(action) in str(i.name)
                is_filters_match = item.exists()

                if is_sender_match and is_action_match and is_filters_match:
                    messages['type'] = action

                    if action == 'change':
                        get_changed_fields(sender, instance, Model, messages)

                    new_alert = Alert.objects.create(object_id=instance.id, content_type=content_type,
                                                     messages=messages)
                    if users:
                        new_alert.users.set(users)
                    if groups:
                        new_alert.groups.set(groups)
                    new_alert.save()
