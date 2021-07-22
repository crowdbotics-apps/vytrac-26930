from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User

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

description = """
# [lookups](https://docs.djangoproject.com/en/3.2/ref/models/lookups/)
1. `gt` = greater than
2. `lt` = less than
3. `e` = or equal 'this can be used `__gte` which mean greater than or equal to' or you can say `lte` which mean less than or equal to  
4. `contains` = this can be used for list like '?groups__contains=providers' in which groups=['doctors','providers']
4. `in` = this check if one value is in many values just the opposite way of contains,
    - example
     1. `user__in=[1,2,3]`
     2. `user__username__in=AliJesusNikolina` you can also check if string is part of a bigger string  

5. `fieldname__sumfielname` = this used for subfields like you can say `column__name=anyname` to get all columns with subobjs that have name = anyname 
    - example
    ```
    {
    "column":{
        "name":"anyname","value":"anyvalue"
    }
    }
    ```
6. `name__icontains` i stand for "case insensitive"
6. `ordering`
    - example1 `?ordering=-id` you will get the order object flipped
    - example2 `?ordering=name` you will get the objects order alphabetically A-Z by the filed called `name`
    - example3 `?ordering=-name` you will get the objects order alphabetically Z-A by the filed called `name`
6. you can add `latest=true`, `earliest=true` to get the latest or earliest object in case it have a field `date_created`
7. `fields=<fieldname>,<fieldname><..>`,
    - example: `?fields=username,id,` this will filter out all other fields 

_____________________________________________________
- `"fieldname=F('modelname__fieldname')"`: this called F expression in django and I return dynamic value.
- example:
    if you have data like this
    ```
    {
    "field_value":"22"
    "column":{min:'22', max:'33'}
    },
    {
    "field_value":"300"
    "column":{min:'22', max:'33'}
    }
    ```
- `url/?field_value__lte=F('column__min')` this will return only 
    ```
    {
    "field_value":"22"
    "column":{min:'22', max:'33'}
    }
    ```

______________________________________________
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


# swagger
api_info = openapi.Info(
    title="DjangoTests API",
    default_version="v1",
    description=description,
)

schema_view = get_schema_view(
    api_info,
    public=True,
    # permission_classes=(permissions.IsAuthenticated,),
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="api_docs"),
    path('docs/', include_docs_urls(title='VYTRAC🏥', description=description)),
]


urlpatterns += [path("", TemplateView.as_view(template_name='index.html'))]
urlpatterns += [re_path(r"^(?:.*)/?$",TemplateView.as_view(template_name='index.html'))]
