from .. import models
from Functions.DynamicSer import DynamicSerializer
from Functions.MyViews import ItemsView

MyModel = models.AllDataStr


class ModelSer(DynamicSerializer):
    class Meta:
        model = MyModel
        fields = '__all__'


class Views(ItemsView):
    queryset = MyModel.objects.all()
    serializer_class = ModelSer

# del Views.post #TODO delete method post without effecting the others