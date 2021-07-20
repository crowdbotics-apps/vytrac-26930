from django.urls import path
from users import Usersviews
from rest_framework_simplejwt.views import (
    TokenRefreshView, TokenVerifyView
)

from .auth.views import  LoginView, LogoutView, RequestPasswordResetEmail, SetNewPasswordAPIView, \
    VerifyEmail
from .views import userssettings, Availability, address, Notes


urlpatterns = [
    path('usersettings/', userssettings.Views.as_view(), name="usersettings"),
    path('usersettings/<int:pk>/',
         userssettings.View.as_view(), name='userettings'),

    # path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='verfy_token'),

    path('request-reset-email/', RequestPasswordResetEmail.as_view(),
         name="request-reset-email"),
    path('password-reset-complete/', SetNewPasswordAPIView.as_view(),
         name='password-reset-complete'),
    path('verify_email/', VerifyEmail.as_view(), name="email-verify"),

    path('', Usersviews.UsersView.as_view(), name='all_users'),
    path('<int:pk>/', Usersviews.UserView.as_view(), name='user_url'),

    path('availability', Availability.Views.as_view(), name='availablities'),
    path('Availability/<int:pk>/', Availability.View.as_view(), name='availability'),
    path('address', address.Views.as_view(), name='addresses'),
    path('address/<int:pk>/', address.View.as_view(), name='address'),
    path('notes', Notes.Views.as_view(), name='notes'),
    path('notes/<int:pk>/', Notes.View.as_view(), name='notes'),

    # path('groups/', Usersviews.UsersView.as_view(), name='all_users'),
    # path('groups/<int:pk>/', Usersviews.UserView.as_view(), name='get, update'),

]
