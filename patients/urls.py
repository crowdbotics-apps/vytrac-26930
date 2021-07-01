
from django.urls import path

from .views import roster, payment, patients, Emergency_contact, SymptomsHistory, Disease, RPMplan

urlpatterns = [

    path('emergency_contact/', Emergency_contact.Views.as_view(), name='Emergency_contacts'),
    path('emergency_contact/<int:pk>/', Emergency_contact.View.as_view(), name='Emergency_contact'),

    path('rosters/', roster.Views.as_view(), name='rosters'),
    path('rosters/<int:pk>/', roster.View.as_view(), name='roster'),

    path('billings/', payment.Views.as_view(), name='billings'),
    path('billings/<int:pk>/', payment.View.as_view(), name='billing'),

    path('', patients.Views.as_view(), name='PationtsView'),
    path('<int:pk>/', patients.View.as_view(), name='PationtsView'),
    path('symptoms', SymptomsHistory.Views.as_view(), name='Symptoms'),
    path('symptoms/<int:pk>/', SymptomsHistory.View.as_view(), name='Symptom'),
    path('diseases', Disease.Views.as_view(), name='Diseases'),
    path('diseases/<int:pk>/', Disease.View.as_view(), name='Disease'),
    path('RPMplan', RPMplan.Views.as_view(), name='RPMplans'),
    path('RPMplan/<int:pk>/', RPMplan.View.as_view(), name='RPMplan'),


]
