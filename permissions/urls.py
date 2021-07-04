from django.contrib.auth.models import Group, Permission
from django.urls import path
from rest_framework import generics, status
from rest_framework.response import Response

from Functions.DynamicSer import DynamicSerializer
from Functions.MyViews import ItemView, ItemsView
from Functions.queryset_filtering import queryset_filtering

MyModel = Group

# TODO create permissions issue from front end
class GroupSer(DynamicSerializer):
    class Meta:
        model = MyModel
        fields = '__all__'


class GroupsView(ItemsView):
    queryset = MyModel.objects.all()
    serializer_class = GroupSer


class GroupView(ItemView):
    queryset = MyModel.objects.all()
    serializer_class = GroupSer


class PermissionsModelSer(DynamicSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class PermissionsView(generics.ListAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionsModelSer
    def get(self, request, *args, **kwargs):
        context = {'request': request, 'method': 'view'}

        items = queryset_filtering(self.queryset.model, request.GET)
        serializer = self.serializer_class(
            items, context=context, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

urlpatterns = [
    path('', GroupsView.as_view(), name='groups'),
    path('<int:pk>/', GroupView.as_view(), name='group'),
    path('all_permissions/', PermissionsView.as_view(), name='all_permissions'),
]


# @Receiver(signals , sender=User)
# def my_handler(sender, **kwargs):
#     TODO if 'can_change_smth'in instance.user_permissions then set'can_view_smth'
