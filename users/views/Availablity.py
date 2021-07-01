from Functions.MyViews import ItemView, ItemsView
from .. import models
from Functions.DynamicSer import DynamicSerializer

MyModel = models.Availablity


class ModelSer(DynamicSerializer):
    class Meta:
        model = MyModel
        fields = '__all__'


class Views(ItemsView):
    queryset = MyModel.objects.all()
    serializer_class = ModelSer

    def post(self,*args,**kwargs):
        """
        var params = {
        title: "<str>",
        description: '<str>',
        start: '<yyyy-mmm-dddTHH:MM:SS.FF>',
        end: '<yyyy-mmm-dddTHH:MM:SS.FF>',
        recurrence: ['str','stre'],
        user:<id>,
        }

        """
        return super().post(*args,**kwargs)


class View(ItemView):
    MyModel = MyModel
    queryset = MyModel.objects.all()
    serializer_class = ModelSer
    # TODO test this
    def get_queryset(self,pk,request,*args,**kwargs):
        setattr(request,'is_owner',MyModel.objects.get(id=pk).user == request.user)
        return super().get(pk,request,*args,**kwargs)
