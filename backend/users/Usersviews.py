##
from django.contrib.auth.models import Group
from django.contrib.sites.shortcuts import get_current_site
from icecream import ic
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from Functions.MyViews import ItemView, ItemsView
from Functions.Permissions import permision_chack, get_user_permissions
##
from Functions.id_getter import ids_getter, id_getter
from Functions.typost_check import typos_check
from users import serializers, auth
from .models import User
from .serializers import UserSerForAddmin
from django.template.loader import render_to_string

from django.urls import reverse

from .utils import Util


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

        pk = kwargs.get('pk')
        setattr(self.request, 'is_owner', pk == self.request.user.id)
        self.serializer_class = serializers.UpdateUsersSerializer

        # user = self.request.user
        # permissions = get_user_permissions(user)
        # is_permited = 'add_user' or 'update_user' or 'update_email' in permissions

        # if not (is_permited or user.is_staff or user.is_superuser):
        #     self.serializer_class = serializers.UpdateUsersSerializer
        # else:
        #     self.serializer_class = UserSerForAddmin

        groups_names = self.request.data.get('groups')

        if groups_names:
            groups_ids = ids_getter(Group, groups_names, 'name')
            if groups_ids['success']:
                self.request.data['groups'] = groups_ids['data']
            else:
                return Response(groups_ids['data'], status=status.HTTP_400_BAD_REQUEST)
        return super().put(*args,**kwargs)

class UsersView(ItemsView):
    """
    - Note: `domain.com/users/?groups__conainets=patient` to get all patients instead of all uses
    - the patient roster is relational data so any user profile can be a aptient roster in case `groups__conainets=patient`
    """

    def post(self, request):
        self.serializer_class = serializers.RegisterSerializer
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user).access_token
        current_site = get_current_site(request).domain
        relativeLink = reverse('email-verify')

        link = 'http://' + current_site + relativeLink + "?token=" + str(token)
        email_body = render_to_string("verify_email.html", {'name': user.username, 'link': link})
        data = {'email_body': email_body, 'to_email': user.email,
                'email_subject': 'Verify your email'}

        Util.send_email(data)
        return Response(user_data, status=status.HTTP_201_CREATED)

    queryset = User.objects.all()
    serializer_class = serializers.UsersSerializer


