from django.conf import settings
from django.db import models
from safedelete.models import SafeDeleteModel


# from patients.models.models import Patient, Symptom #TODO this is circular


class Column(SafeDeleteModel):
    max = models.PositiveIntegerField(max_length=500, null=True, blank=True)
    min = models.PositiveIntegerField(max_length=500, null=True, blank=True)
    limit = models.PositiveIntegerField(max_length=500, null=True, blank=True,
                                        help_text='if {absolute(latest measurement - the new measurement) == limit} then you may need to be alerted')
    name = models.CharField(max_length=500)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='statistics', null=True, on_delete=models.SET_NULL)

    @property
    def is_equal_to_limit(self):
        return False
        # self.value.objects.last().fied_value - self.value.earliest().fiedl_value


# class BaseModel(SafeDeleteModel):


class Value(SafeDeleteModel):
    object_id = models.CharField(max_length=20)
    name = models.CharField(max_length=50, blank=True)
    column = models.ForeignKey(Column, related_name='values', on_delete=models.CASCADE)
    #TODO use regex to field_value__iregex=(\d+)(\/)($$>90)
    field_value = models.CharField(max_length=500)
    #TODO remove action
    RCHOICES = (
        ('added', 'added'),
        ('changed', 'changed'),
        ('deleted', 'deleted'),
    )
    action = models.CharField(choices=RCHOICES, max_length=50, blank=True)
    seen_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='seen_by_users', blank=True)
    date_created = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        get_latest_by = 'date_created'

# 1. interactions with daly palns
# 2. clicks or wahtever

# @receiver(signals.pre_save, sender=Patient)
# def __init__(instance, update_fields, sender, *args, **kwargs):
#     try:
#         old_object = Patient.objects.get(id=instance.id)
#         for index, item in enumerate(old_object._meta.fields):
#             field_target = item.name
#             field_value = str(getattr(instance, field_target))
#             old_field_value = str(getattr(old_object, field_target))
#             # TODO symptoms
#             # print('======================')
#             # print(instance.symptoms.all =())
#             # print(old_object.symptoms.all())
#             # print('======================')
#             if (old_field_value != field_value):
#                 # TODO realted_to = patients.user
#                 ChangeTrack.objects.create(action_type='changed', model_target=str(
#                     'patients'), field_value=field_value, field_target=field_target, object_id=instance.id)
#     except:
#         pass


# @receiver(signals.post_save, sender=Patient)
# def __init__(instance, created, update_fields, sender, *args, **kwargs):
#     if (created):
#         for index, item in enumerate(instance._meta.fields):
#             field_target = item.name
#             field_value = str(getattr(instance, field_target))
#             # TODO realted_to = patients.user
#             ChangeTrack.objects.create(action_type='added', model_target=str(
#                 'DateType'), field_value=field_value, field_target=field_target, object_id=instance.id)
