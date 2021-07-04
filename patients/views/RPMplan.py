from Functions.MyViews import ItemView, ItemsView
from Functions.DynamicSer import DynamicSerializer
from patients import models

MyModel = models.RPMplan


class RelationalRPMplanSer(DynamicSerializer):
    # muserments #TODO
    class Meta:
        model = MyModel
        fields = ['name','description','muserments']

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
