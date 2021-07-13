from django.urls import path
from .views import home, frontend

urlpatterns = [
    path("", frontend, name="home"),
]
