from django.contrib import admin
from django.urls import path, include
from allauth.account.views import confirm_email
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework.routers import DefaultRouter

# load api urls
from home.api.v1.urls import router as home_router
router = DefaultRouter()

router.registry.extend(home_router.registry)

urlpatterns = [
    path("", include("home.urls")),
    # path("accounts/", include("allauth.urls")),
    # path("modules/", include("modules.urls")),
    path("api/v1/", include("home.api.v1.urls")),
    path("admin/", admin.site.urls),
    # path("users/", include("users.urls", namespace="users")),
    path("rest-auth/", include("rest_auth.urls")),
    # Override email confirm to use allauth's HTML view instead of rest_auth's API view
    path("rest-auth/registration/account-confirm-email/<str:key>/", confirm_email),
    path("rest-auth/registration/", include("rest_auth.registration.urls")),
]

admin.site.site_header = "VyTrac"
admin.site.site_title = "VyTrac Admin Portal"
admin.site.index_title = "VyTrac Admin"

# swagger
api_info = openapi.Info(
    title="VyTrac API",
    default_version="v1",
    description="API documentation for VyTrac App",
)

schema_view = get_schema_view(
    api_info,
    public=True,
    permission_classes=(permissions.IsAuthenticated,),
)

urlpatterns += [
    path("api-docs/", schema_view.with_ui("swagger", cache_timeout=0), name="api_docs")
]
