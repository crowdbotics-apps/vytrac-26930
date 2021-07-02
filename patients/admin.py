from django.contrib import admin

from patients.models import models

admin.site.register(models.Patient)
admin.site.register(models.Symptom)
admin.site.register(models.Reports)
admin.site.register(models.Conditions)
admin.site.register(models.SymptomsHistory)
admin.site.register(models.Disease)
