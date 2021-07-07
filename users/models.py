import pytz
from django.conf import settings
from django.contrib.auth.models import Permission
from django.contrib.auth.models import User, AbstractUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from safedelete import SOFT_DELETE
from safedelete.models import (
    SafeDeleteModel
)

from Functions.MyViews import Rec

StyleTitleFormat = RegexValidator(r'^[^\s]+$', 'spaces not allowed')

# @Receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)


PHONE_NUMBER_REGEX = RegexValidator(
    r'^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$', 'invalid phone number')

USERNAME = RegexValidator(
    r'^[a-zA-Z ]+$', 'only letter from a-z are allowed')

REC = (
    ('0 G day', 'Every day.'),

)


class Availablity(SafeDeleteModel):
    title = models.CharField(max_length=999, null=True, blank=True)
    description = models.TextField(max_length=9999, blank=True, null=True)
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='availablity', on_delete=models.CASCADE)
    recurrence = Rec(blank=True, choices=REC)

    class Meta:
        get_latest_by = 'date_created'


models_names = (('patien profiel', 'patien profiel'),)


class Settings(SafeDeleteModel):
    # notifcaions settings/report settings
    #
    watch = models.CharField(max_length=50, choices=models_names, blank=True)
    settings_type = models.CharField(max_length=999, choices=(
        ('notifcations', 'notifcations settings'), ('reporet', 'reporet tashbord settings')), unique=True)
    see_all = models.BooleanField(default=False)


class Sex(models.Model):
    name = models.CharField(max_length=50, blank=True)



class User(AbstractUser, PermissionsMixin):
    import pytz
    timezones = []
    for tz in pytz.all_timezones:
        zone = tz
        # offset = pytz.timezone(tz).utcoffset(datetime.now())
        # now = datetime.now(tz=pytz.UTC).astimezone(pytz.timezone(tz))
        timezones.append((tz,tz))
    _safedelete_policy = SOFT_DELETE
    timezone = models.CharField(choices=timezones, max_length=99, blank=True)
    is_archived = models.BooleanField(default=False)

    photo = models.ImageField(blank=True, null=True)

    username = models.CharField(
        max_length=30, unique=True, validators=[USERNAME], blank=True)
    email = models.EmailField(max_length=250, unique=True,blank=True)
    secon_email = models.EmailField(max_length=250, blank=True)
    # unique=True #TODO

    sex = models.ManyToManyField(Sex, related_name='user_sex', blank=True)
    first_name = models.CharField(max_length=999, blank=True, null=True)
    last_name = models.CharField(max_length=999, blank=True, null=True)
    middle_name = models.CharField(max_length=999, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    is_role_verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    receive_newsletter = models.BooleanField(default=False)
    birth_date = models.DateTimeField(blank=True, null=True)
    # address = AddressField(related_name='+', blank=True, null=True)
    city = models.CharField(max_length=999, blank=True, null=True)
    about_me = models.TextField(max_length=500, blank=True, null=True)
    phone_number = models.TextField(
        max_length=500, blank=True, null=True, validators=[PHONE_NUMBER_REGEX])

    second_phone_number = models.TextField(
        max_length=500, blank=True, null=True, validators=[PHONE_NUMBER_REGEX])
    imageUrl = models.CharField(max_length=900, blank=True, null=True)
    # TODO if not avablae then you can't create apoentment
    settings = models.ManyToManyField(Settings, related_name='who_can_see_comment', blank=True)
    age = models.CharField(max_length=50, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]
    class Meta:
        get_latest_by = 'date_created'


class Address(SafeDeleteModel):
    home = models.CharField(max_length=999, unique=True)
    apt = models.CharField(max_length=999, unique=True)
    state = models.CharField(max_length=999, unique=True)
    zip_code = models.CharField(max_length=999, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='address',on_delete=models.SET_NULL, null=True, blank=True, unique=True)

class Note(SafeDeleteModel):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2000, null=True, blank=True)
    alert_date = models.DateTimeField(help_text='specify time to remind you about this note', null=True, blank=True)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='notes', blank=True)
