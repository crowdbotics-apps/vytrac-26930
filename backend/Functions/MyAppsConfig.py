from django.apps import AppConfig
from icecream import ic

from Functions.make_fields_permissions import make_fields_permissions

allData = []


def create_all_data_str(Permission, AllDataStr):
    for i in Permission.objects.all():
        is_valid = ('Can view' not in i.name) and ('alert' not in i.name) and ('all data str' not in i.name) and (
                    'alldatastr' not in i.name)
        if is_valid:
            i.name = i.name.replace('Can ', '')
            newdata, created = AllDataStr.objects.get_or_create(name=i.name, codename=i.codename)
            newdata.content_type = i.content_type
            newdata.save()


class YourAppConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'Functions.MyAppsConfig'

    def ready(self):
        from django.contrib.auth.models import Permission
        from django import apps
        from Alerts.models import AllDataStr, AlertRule
        from django.contrib.contenttypes.models import ContentType

        for Model in apps.apps.get_models():
            try:
                make_fields_permissions(Permission, ContentType, Model)
            except:
                pass

        try:
            create_all_data_str(Permission, AllDataStr)
        except:
            pass
            # ic('no such table: auth_permission')
