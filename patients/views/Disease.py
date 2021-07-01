from Functions.MyViews import ItemView, ItemsView
from Functions.DynamicSer import DynamicSerializer
from patients.models import models

MyModel = models.Disease


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
