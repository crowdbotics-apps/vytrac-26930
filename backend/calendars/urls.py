from django.urls import path
from icecream import ic
from rest_framework import serializers

from Functions.MyViews import ItemsView, ItemView
from . import models
from .serializers import CalinderSeriazliser

# TODO Availability

MyModel = models.Event


class DateSer(serializers.ModelSerializer):
    # TODO recurrence = serializers.ChoiceField(Required=False)
    class Meta:
        model = MyModel
        fields = '__all__'


class CalindersView(ItemsView):
    queryset = MyModel.objects.all()
    serializer_class = CalinderSeriazliser

    def post(self, *args, **kwargs):
        self.request.data['created_by'] = self.request.user.id
        return super().post(*args, **kwargs)


class CalinderView(ItemView):
    queryset = MyModel.objects.all()
    serializer_class = CalinderSeriazliser


urlpatterns = [
    path('', CalindersView.as_view(), name="calinders"),
    path('<int:pk>/', CalinderView.as_view(), name="calinder"),
    # path('', TypesView.as_view(), name="date_types"),
    # path('<int:pk>/', TyperView.as_view(), name="date_type"),
]
