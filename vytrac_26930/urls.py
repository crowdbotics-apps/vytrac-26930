from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, generics
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v2',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

description = """
# [lookups](https://docs.djangoproject.com/en/3.2/ref/models/lookups/)
1. `gt` = greater than
2. `lt` = less than
3. `e` = or equal 'this can be used `__gte` which mean greater than or equal to' or you can say `lte` which mean less than or equal to  
4. `contains` = this can be used for list like '?groups__contains=providers' in which groups=['doctors','providers']
4. `in` = this check if one value is in many values just the oppist way of contains,
    - example
     1. `user__in=[1,2,3]`
     2. `user__username__in=AliJesusNikolina` you can also check if string is part of a bigger string  
5. `fieldname__sumfielname` = this used for subfields like you can say `column__name=anyname` to get all columns with subobjs that have name = anyname 
6. you can add `latest=true`, `earlist=true` to get the laties or earlist object in case it have a field `date_created`
        - example
        
        ```
        {
        "column":{
            "name":"anyname","value":"anyvalue"
        }
        }
        ```
7. `fields=<fieldname>,<fieldname><..>`,
    - example: `?fields=username,id,` this will filter out all other fields 
        
        

# headers
- authentication
        ```
        headers = {
        'Authorization': 'Bearer <token>',
        }
        ```
"""

user = None
try:
    user = User.objects.earliest()
except:
    pass

try:
    token = RefreshToken.for_user(user).access_token
    description += f"""
# dummy login
    - `username = {user.username}`
    - `password = password`
    - `token={str(token)}`
"""
except:
    pass


urlpatterns = [
    path('', include_docs_urls(title='Vytrac',description=description)),
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
