from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.documentation import include_docs_urls

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),

    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include_docs_urls(title='Vytrac',description='All endpoints have filtering functionalities like fieldName__gte=<val>, fieldName__contains=<str>, fieldName__subfieldName__gte=<val>, also you can add "latest=true, earlist=true to get the laties/earlist object')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('calendars/', include('calendars.urls')),
    path('patient/', include('patients.urls')),
    path('groups/', include('permissions.urls')),
    path('statistics/', include('timesheets.urls')),
    path('tasks/', include('tasks.urls')),
    path('automation/', include('automations.urls')),
    path('alerts/', include('Alerts.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
