from icecream import ic
from rest_framework import serializers
from rest_framework.serializers import (
    ModelSerializer,
)

from Functions.DynamicSer import DynamicSerializer
from patients.views import patients, SymptomsHistory
from patients.views.RPMplan import RelationalRPMplanSer
from patients.views.book_services import RelationalBookingSer
from timesheets.urls import StaSer
from .models import User, Availability
from .password_validator import PasswordValidatorSer
from .views.address import RelationaladdressSer


class AvalibitlySer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(many=False, read_only=True, slug_field='username')

    class Meta:
        model = Availability
        fields = '__all__'


class RelationalAvalibitlySer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = ['title', 'description', 'start', 'end', 'recurrence']


class UpdateSer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'name',
            'designation',
            'is_active',
            'is_superuser',
            'is_staff',
        )


class UserSerForAddmin(PasswordValidatorSer, DynamicSerializer):
    email = serializers.EmailField(required=False)
    username = serializers.CharField(required=False)
    password = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = '__all__'


class RegisterSerializer(PasswordValidatorSer, ModelSerializer):
    timezones = []
    username = serializers.CharField(max_length=555, required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    default_error_messages = {'username': 'The username should only contain alphanumeric characters'}

    class Meta:
        model = User
        fields = ["password",
                  "timezone",
                  "photo",
                  "username",
                  "email",
                  "secon_email",
                  "first_name",
                  "last_name",
                  "middle_name",
                  "is_active",
                  "is_staff",
                  "is_role_verified",
                  "receive_newsletter",
                  "birth_date",
                  "city",
                  "about_me",
                  "phone_number",
                  "second_phone_number",
                  "imageUrl",
                  "groups", ]


class UsersSerializer(PasswordValidatorSer, DynamicSerializer):

    statistics = StaSer(many=True, read_only=True)
    patient_profile = patients.ModelSer(many=False, read_only=True)
    symptoms_history = SymptomsHistory.SymtomsHistorySer(many=True, read_only=True)
    availability = RelationalAvalibitlySer(many=True, read_only=True)
    address = RelationaladdressSer(many=False, read_only=True)
    booked_services = RelationalBookingSer(many=True, read_only=True)
    RPMplan = RelationalRPMplanSer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [*[x.name for x in User._meta.fields], 'events', 'patient_profile', 'statistics', 'symptoms_history',
                  'availability', 'address', 'RPMplan', 'booked_services', 'groups']



class UpdateUsersSerializer(PasswordValidatorSer, DynamicSerializer):
    password = serializers.CharField(max_length=68, min_length=6, required=False)

    class Meta:
        model = User
        fields = '__all__'
