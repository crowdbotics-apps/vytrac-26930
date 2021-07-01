from django.urls import path
from rest_framework import generics
from .views import alertsRules, SeenBy, trigers


class AlertsView(generics.ListAPIView):
    """
    #`ws://domain/alerts/?token=<token>`
    <h1 class="label label-primary">connect</h1>
    - "convential I should name it notifcations"

    <h1 class="label label-primary">onmessage</h1>
    - None

    <h1 class="label label-primary">send</h1>
        ```
            {target:'events', id:1, is_seen:true}
        ```
    - note quereis and filters als work here.
    """
    pass


urlpatterns = [
    # path('', admin.site.urls),
    path('', AlertsView.as_view(), name='alerts view'),
    path('rules/', alertsRules.Views.as_view(), name='alerts rules'),
    path('rules/<int:pk>/', alertsRules.View.as_view(), name='alerts rule'),

    path('seen_by/', SeenBy.Views.as_view(), name='SeenBys'),
    path('seen_by/<int:pk>/', SeenBy.View.as_view(), name='SeenBy'),
    path('trigers/', trigers.Views.as_view(), name='trigers'),

]
