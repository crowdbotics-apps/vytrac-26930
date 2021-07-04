from rest_framework import serializers

from Functions.MyViews import ItemView, ItemsView
from Functions.DynamicSer import DynamicSerializer
from patients import models

MyModel = models.SymptomsHistory


class ModelSer(DynamicSerializer):
    class Meta:
        model = MyModel
        fields = '__all__'


class SymtomsHistorySer(DynamicSerializer):
    symptoms = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')

    class Meta:
        model = MyModel
        fields = ['date_created', 'symptoms']


class Views(ItemsView):
    queryset = MyModel.objects.all()
    serializer_class = ModelSer


class View(ItemView):
    MyModel = MyModel
    queryset = MyModel.objects.all()
    serializer_class = ModelSer
