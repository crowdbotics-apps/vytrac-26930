from rest_framework import serializers
from rest_framework.serializers import (
    ModelSerializer,
)

from Functions.DynamicSer import DynamicSerializer
from patients.views import patients, SymptomsHistory
from patients.views.RPMplan import RelationalRPMplanSer
from patients.views.book_services import RelationalBookingSer
from timesheets.urls import StaSer
from .models import User, Availablity
from .views.address import RelationaladdressSer


class AvalibitlySer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(many=False, read_only=True, slug_field='username')

    class Meta:
        model = Availablity
        fields = '__all__'


class RelationalAvalibitlySer(serializers.ModelSerializer):
    class Meta:
        model = Availablity
        fields = ['title','description','start','end','recurrence']


class UserUpdateSer(ModelSerializer):
    username = serializers.CharField(max_length=555)

    class Meta:
        fields = ['username', ]


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


class UserSerForAddmin(DynamicSerializer):
    email = serializers.EmailField(required=False,allow_blank=True)
    username = serializers.CharField(required=False,allow_blank=True)
    password = serializers.CharField(required=False,allow_blank=True)
    class Meta:
        model = User
        fields = '__all__'



class UsersSerializer(DynamicSerializer):
    statistics = StaSer(many=True, read_only=True)
    patient_profile = patients.ModelSer(many=False, read_only=True)
    symptoms_history = SymptomsHistory.SymtomsHistorySer(many=True, read_only=True)
    availablity = RelationalAvalibitlySer(many=True, read_only=True)
    address = RelationaladdressSer(many=False, read_only=True)
    booked_services = RelationalBookingSer(many=True, read_only=True)
    RPMplan = RelationalRPMplanSer(many=True,read_only=True)

    class Meta:
        model = User
        fields = [*[x.name for x in User._meta.fields], 'events', 'patient_profile','statistics','symptoms_history','availablity','address','RPMplan','booked_services','groups']


class UpdateUsersSerializer(DynamicSerializer):
    class Meta:
        model = User
        fields = ["password",
                  "last_login",
                  "photo",
                  "secon_email",
                  "first_name",
                  "last_name",
                  "middle_name",
                  "receive_newsletter",
                  "birth_date",
                  "city",
                  "about_me",
                  "phone_number",
                  "second_phone_number",
                  "imageUrl",
                  "age",
                  # "address"
                  ]
