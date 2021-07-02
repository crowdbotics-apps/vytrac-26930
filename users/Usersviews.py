##
from icecream import ic
from rest_framework import permissions, status
from rest_framework.response import Response

from Functions.MyViews import ItemView, ItemsView
from Functions.Permissions import permision_chack, get_user_permissions
##
from users import serializers
from .models import User
from .serializers import UserSerForAddmin


class WhoCanView(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff


class IsActive(permissions.BasePermission):
    message = ''

    def has_permission(self, request, view):
        message = permision_chack('view', 'user', request.user)['message']
        return permision_chack('view', 'user', request.user)['is_premited']


class UserView(ItemView):
    MyModel = User
    queryset = User.objects.all()
    serializer_class = serializers.UsersSerializer

    def get(self, request, pk):
        setattr(request,'is_owner',pk == request.user.id)
        return super().get(request, pk,)

    def put(self, *args,**kwargs):
        user = self.request.user
        permissions = get_user_permissions(user)
        is_permited = 'add_user' or 'update_user' or 'update_email' in permissions

        if not (is_permited or user.is_staff or user.is_superuser):
            self.serializer_class = serializers.UpdateUsersSerializer
        else:
            self.serializer_class = UserSerForAddmin
        return super().put(*args,**kwargs)

class UsersView(ItemsView):
    """
    - Note: `domain.com/users/?groups__conainets=patient` to get all patients instead of all uses
    - the patient roster is relational data so any user profile can be a aptient roster in case `groups__conainets=patient`
    """
    queryset = User.objects.all()
    serializer_class = serializers.UsersSerializer
    search_fields = '__all__'


