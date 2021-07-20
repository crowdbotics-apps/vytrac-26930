from django.contrib import admin

#
from . import models

admin.site.register(models.User)
admin.site.register(models.Availability)
admin.site.register(models.Settings)
admin.site.register(models.Note)


# potnetially we may need to keep group named group.
# admin.site.register(models.User)
# admin.site.register(models.Other)
# admin.site.register(models.Other)
# admin.site.register(models.Other)
