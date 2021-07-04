from django.contrib.auth.models import Group
from icecream import ic
from rest_framework import serializers, status
from rest_framework.response import Response

from users.models import User
from .. import models
from Functions.DynamicSer import DynamicSerializer
from Functions.MyViews import ItemView, ItemsView
from ..models import AllDataStr, AlertRule

MyModel = models.AlertRule

class RelationalAlertRulelSer(DynamicSerializer):
    trigers = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
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
            - if user oxgyen level__lt=80 then notify doctors and providers
                params = {
                "object_id": '',
                "filter": '__lt=80',
                "field_value": ...,
                "priority": ...,
                "trigers": [235],
                # for trigers go to /alerts/trigers/?content_type__model=value&codename__contains=field_value
                # then copy the id and add it to the trigers list
                "users": [1,2,3],
                "groups": ['doctors', 'providers',], // Note : groups you can mention them by name instead of id
                }

        """
        groups = request.data.get('groups')
        trigers = request.data.get('trigers')
        groups_ids = []
        if(groups):
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

        # trigers_ids = []
        #
        # if trigers:
        #     for i in trigers:
        #         try:
        #             triger = AllDataStr.objects.get(name=i)
        #             trigers_ids.append(triger.id)
        #         except:
        #             return Response(f"You may have a typo in the triger name {i}", status=status.HTTP_400_BAD_REQUEST)
        #     request.data['trigers'] = trigers_ids
        # else:
        #     request.data['trigers'] = []
        return super().post(request,*args,**kwargs)




    queryset = MyModel.objects.all()
    serializer_class = ModelSer


class View(ItemView):
    MyModel = MyModel
    queryset = MyModel.objects.all()
    serializer_class = ModelSer
