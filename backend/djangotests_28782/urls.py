"""djangotests_28782 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView
from allauth.account.views import confirm_email
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

urlpatterns = [
    path("", include("home.urls")),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('calendars/', include('calendars.urls')),
    path('patient/', include('patients.urls')),
    path('groups/', include('permissions.urls')),
    path('statistics/', include('timesheets.urls')),
    path('tasks/', include('tasks.urls')),
    path('automation/', include('automations.urls')),
    path('alerts/', include('Alerts.urls')),
    path('archive/', include('archive.urls')),
]

admin.site.site_header = "DjangoTests"
admin.site.site_title = "DjangoTests Admin Portal"
admin.site.index_title = "DjangoTests Admin"

# swagger
api_info = openapi.Info(
    title="DjangoTests API",
    default_version="v1",
    description="API documentation for DjangoTests App",
)

schema_view = get_schema_view(
    api_info,
    public=True,
    permission_classes=(permissions.IsAuthenticated,),
)

urlpatterns += [
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="api_docs")
]


urlpatterns += [path("", TemplateView.as_view(template_name='index.html'))]
urlpatterns += [re_path(r"^(?:.*)/?$",
                TemplateView.as_view(template_name='index.html'))]
