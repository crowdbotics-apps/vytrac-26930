from django.contrib.auth.models import Group
from icecream import ic
from rest_framework import serializers, status
from rest_framework.response import Response

from Functions.DynamicSer import DynamicSerializer
from Functions.MyViews import ItemView, ItemsView
from .. import models

MyModel = models.AlertRule

class RelationalAlertRulelSer(DynamicSerializer):
    triggers = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    class Meta:
        model = MyModel
        fields = '__all__'


class ModelSer(DynamicSerializer):
    class Meta:
        model = MyModel
        fields = '__all__'


class Views(ItemsView):
    def post(self,request,*args,**kwargs):
        """
# Quick example:
    - if user oxygen level__lt=80 then notify doctors and providers
           # TODO organize this
           ``` params = {
            "object_id": '',
            "filters": '
            {
            "column__name":"oxygen",
            "field_value__lt":"80"
            },
            "triggers": [235],}```
            # patient
            # for triggers go to /alerts/triggers/?content_type__model=value&codename__contains=field_value
            # then copy the id and add it to the triggers list
            "users": [1,2,3],
            "groups": ['doctors', 'providers',], // Note : groups you can mention them by name instead of id
            }

    - if you want to watch the oxygen level of a specific patient. In filters, you can add `"column__user":"2"` where 2 is <user.id>
- if you want to get alerted only when delete an event that not ended yet? `"filters":{"end__lte":"now"},`
    """

        groups = request.data.get('groups')
        groups_ids = []
        if groups:
            for g in groups:
                try:
                    group = Group.objects.get(name=g)
                    groups_ids.append(group.id)
                    # groups_objects.append(group)
                except:
                    return Response(f"You may have a typo in the group name {g}", status=status.HTTP_400_BAD_REQUEST)
            request.data['groups'] = groups_ids
        else:
            request.data['groups'] = []

        # triggers_ids = []
        #
        # if triggers:
        #     for i in triggers:
        #         try:
        #             triger = AllDataStr.objects.get(name=i)
        #             triggers_ids.append(triger.id)
        #         except:
        #             return Response(f"You may have a typo in the triger name {i}", status=status.HTTP_400_BAD_REQUEST)
        #     request.data['triggers'] = triggers_ids
        # else:
        #     request.data['triggers'] = []
        return super().post(request, *args, **kwargs)




    queryset = MyModel.objects.all()
    serializer_class = ModelSer


class View(ItemView):
    MyModel = MyModel
    queryset = MyModel.objects.all()
    serializer_class = ModelSer
