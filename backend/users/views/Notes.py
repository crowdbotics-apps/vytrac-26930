from datetime import datetime

import pytz
from icecream import ic

from Functions.MyViews import ItemView, ItemsView
from .. import models
from Functions.DynamicSer import DynamicSerializer

MyModel = models.Note


# class RelationalNotesSer(DynamicSerializer):
#     class Meta:
#         model = MyModel
#         fields = ['title...']

class ModelSer(DynamicSerializer):
    class Meta:
        model = MyModel
        fields = '__all__'


class Views(ItemsView):
    queryset = MyModel.objects.all()
    serializer_class = ModelSer


class View(ItemView):
    MyModel = MyModel
    queryset = MyModel.objects.all()
    serializer_class = ModelSer
