from django.contrib import admin
from .models import AlertRule, SeeAlert, SeenBy, Alert

admin.site.register(AlertRule)
admin.site.register(SeeAlert)
admin.site.register(SeenBy)
admin.site.register(Alert)


#
