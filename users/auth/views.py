import re

import jwt
from asgiref.sync import sync_to_async, async_to_sync
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.http.response import HttpResponseRedirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import smart_bytes
from django.utils.http import urlsafe_base64_encode
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from icecream import ic
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import UntypedToken

##
from . import serializers
from ..models import User
from ..utils import Util


class RegisterView(generics.GenericAPIView):
    serializer_class = serializers.RegisterSerializer

    def post(self, request):
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
        email_body = render_to_string(
            "verify_email.html", {'name': user.username, 'link': link})
        data = {'email_body': email_body, 'to_email': user.email,
                'email_subject': 'Verify your email'}

        Util.send_email(data)
        return Response(user_data, status=status.HTTP_201_CREATED)


x = 'helo'


class LoginView(generics.GenericAPIView):
    serializer_class = serializers.MyTokenObtainPairSerializer

    def post(self, request):
        data = request.data
        user = None
        is_phone = 'phone_number' in data and len(data['phone_number']) > 0
        is_email = 'email' in data and len(data['email']) > 0
        is_username = 'username' in data and len(data['username']) > 0
        if (is_phone):
            user = User.objects.get(phone_number=data['phone_number'])
        elif (is_username):
            user = User.objects.get(username=data['username'])
        elif (is_email):
            user = User.objects.get(email=data['email'])

        if (not user.is_email_verified):
            return Response({'error': 'please verfy your email'}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = serializers.LoginUsersSerializer(user, many=False)
        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            # TODO AttributeError: 'UsersSerializer' object has no attribute 'instance'
            'user': serializer.data
        })


user = None
try:
    ic(user)
    user = User.objects.earliest()
    ic(user)
except:
    ic('there are no migrations yet')

try:
    token = RefreshToken.for_user(user).access_token
    LoginView.post.__doc__ = f"""
        - ## dummy login
        - username = {user.username}
        - password = password
        - token={str(token)}
            """
except:
    pass

class VerifyEmail(APIView):
    serializer_class = serializers.EmailVerificationSerializer

    token_param_config = openapi.Parameter(
        'token', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):

        token = request.GET.get('token')

        try:
            token_data = UntypedToken(token)

            user = User.objects.get(id=token_data["user_id"])

            if (user.is_email_verified):
                return HttpResponseRedirect(redirect_to='https://google.com')

            if not user.is_email_verified:
                user.is_email_verified = True
                user.save()
            return Response(
                {'email': 'The user "' + user.username + '" is successfully activated the email ' + user.email},
                status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Activation Expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)


class RequestPasswordResetEmail(generics.GenericAPIView):
    serializer_class = serializers.ResetPasswordEmailRequestSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        email = request.data.get('email', '')

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            front_url = request.data.get('front_url', '')
            if (len(front_url) > 0):
                front_url += '/' if front_url[-1] != '/' else ''
            link = front_url + '?uidb64=' + uidb64 + '?token=' + token
            email_body = render_to_string(
                "reset_password.html", {'name': user.username, 'link': link})
            data = {'email_body': email_body, 'to_email': user.email,
                    'email_subject': 'Reset your password.'}
            Util.send_email(data)
        return Response({'success': 'We have sent you a link to reset your password'}, status=status.HTTP_200_OK)


class SetNewPasswordAPIView(generics.GenericAPIView):
    serializer_class = serializers.SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'message': 'Password reset success'}, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    serializer_class = serializers.LogoutSer

    def post(self, request):
        if (not request.user.id):
            return Response({'error': 'You are already loged out'})
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            return Response({"message": 'Refresh token seccesfully blacklisted.'}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": 'Refresh token alread blacklisted or invialid.'},
                            status=status.HTTP_400_BAD_REQUEST)
