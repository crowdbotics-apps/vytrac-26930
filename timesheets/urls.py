import difflib

from django.urls import path
from rest_framework import status, serializers
from rest_framework.response import Response

from Functions.DynamicSer import DynamicSerializer
from Functions.MyViews import ItemView, ItemsView
from Functions.fields_lookups import fields_lookups
from users.models import User
from .Functions.Statstics import statistics
from .models import Value, Column

MyModel = Value


# Debugging(Value.objects.filter(column__name='vv'), color='green')
# Debugging(Value.objects.all(), color='green')


class ColumnSer(DynamicSerializer):
    class Meta:
        model = Column
        fields = ['name', 'user' ]


class StaSer(DynamicSerializer):
    class Meta:
        model = Column
        fields = ['name', 'values']
        depth = 1

class StatisticSer(DynamicSerializer):
    # column = ColumnSer(many=False, read_only=True, required=False)

    class Meta:
        model = MyModel
        # fields = ['object_id','field_value', 'name', 'action', 'seen_by', 'date_created', 'column',]
        fields = '__all__'
        depth = 1


class Postser(DynamicSerializer):
    class Meta:
        model = MyModel
        fields = '__all__'




# class StatsticsView(ItemsView):
class StatsticsView(ItemsView):
    def get(self, request, *args, **kwargs):
        """
        - # quick example
            1. `"http://vytrac/statistics/?column__name=oxgyn&&field_value__lt=80"`
                -         here you will get only the users with a history of oxygen level that reached under 80
            2. `"http://vytrac/statistics/?column__name=oxgyn&&field_value__lt=80&date_created__gt=2021-06-09"`
                - now instead of getting all the users with a history of low oxygen, will get only the users that have currently or last measurement bellow 80
                - instead of `date_created__gt=2021-06-09` you can say `latest=true` which returns a list of a single object

            3. `"http://vytrac/statistics/?column__name=oxgyn&cal=min&number=10"`
                - you will get the 10 peaks of oxygen values
            4. `"'/statistics/?cal=duration&column__name=oxgyen&column__user=1&intial=80&final=90'"`
                - How long the oxgyn took to change fro 80 to 90
        ## the list view that look like the following as been sacrificed for the sake of aggregation and flexibility
            - ```
            [{
            "name": "blood pressure",
            "user": 1,
            "column": [{
            "field_value": "22",
            "name": "ccc",
            "action": "added",
            "seen_by": [1],
            "date_created": "2021-06-09T10:42:41.458057Z"
            }, {
            "field_value": "44",
            "name": "ddd",
            "action": "added",
            "seen_by": [],
            "date_created": "2021-06-09T10:42:56.582589Z"
            }]
            }, {
            "name": "oxgyn",
            "user": 1,
            "column": [{
            "field_value": "11",
            "name": "",
            "action": "",
            "seen_by": [],
            "date_created": "2021-06-09T10:43:11.271641Z"
            }]
            }]
            ```
        ## the aggrigaction friendly view
            - ```javascript
                [{
                "field_value": "22",
                "name": "ccc",
                "action": "added",
                "seen_by": [1],
                "date_created": "2021-06-09T10:42:41.458057Z",
                "column": {
                "name": "blood pressure",
                "user": 1
                }
                }, {
                "field_value": "44",
                "name": "ddd",
                "action": "added",
                "seen_by": [],
                "date_created": "2021-06-09T10:42:56.582589Z",
                "column": {
                "name": "blood pressure",
                "user": 1
                }
                }, {
                "field_value": "11",
                "name": "",
                "action": "",
                "seen_by": [],
                "date_created": "2021-06-09T10:43:11.271641Z",
                "column": {
                "name": "oxgyn",
                "user": 1
                }
                }]
                ```
        """

        data = super().get(request, *args, **kwargs).data
        getter = request.GET

        if ('cal' in getter) and ('fields' in getter):
            return Response({'error': 'You can not element fields because thy are needed for th calculations'},status=status.HTTP_400_BAD_REQUEST)

        data = statistics(data, getter)
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        column = request.data.get('column')
        is_sure = request.data.get('sure')
        cal_name = request.data['column']['name']

        words = []
        for col in Column.objects.all():
            if cal_name != col.name:
                words.append(col.name)
        words = difflib.get_close_matches(cal_name, words)
        if len(words) > 0 and is_sure != "true":
            return Response({
                'potential typo': 'Did you mean ' + str(words) + '?',
                "note": "If you think you do not have a typo send {'sure' : 'true'} with the data."})


        column, created = Column.objects.get_or_create(name=column['name'], user=User.objects.get(id=column['user']))
        request.data['column'] = column.id
        self.serializer_class = Postser
        return super().post(request, *args, **kwargs)

    queryset = MyModel.objects.all()
    serializer_class = StatisticSer


class StatsticView(ItemView):
    queryset = MyModel.objects.all()
    serializer_class = StatisticSer


urlpatterns = [
    path('', StatsticsView.as_view(), name='Statstics'),
    path('<int:pk>/', StatsticView.as_view(), name=' Statstic'),

]
