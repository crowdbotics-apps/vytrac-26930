from django.urls import path
from rest_framework import generics
from .views import alertsRules, SeenBy, triggers


class AlertsView(generics.ListAPIView):
    """
    #`ws://domain/alerts/?token=<token>`
    <h1 class="label label-primary">connect</h1>
    - "convential I should name it notifcations"

    <h1 class="label label-primary">onmessage</h1>
    - None

    <h1 class="label label-primary">send</h1>
    to tell that the alert with id=1 is seen by the current loged-in user
        ```
            {id:1, is_seen:true}
        ```
    - Note queries and filters also work here.
        - In an additional query you can add `?related_only=tru` this will filter out the unrelated alert for the currened loged-in users
            - this is useful if the user `is_superuser` in which she/he have the option to view all alerts of other users.
    """
    pass


urlpatterns = [
    # path('', admin.site.urls),
    path('', AlertsView.as_view(), name='alerts view'),
    path('rules/', alertsRules.Views.as_view(), name='alerts rules'),
    path('rules/<int:pk>/', alertsRules.View.as_view(), name='alerts rule'),

    path('seen_by/', SeenBy.Views.as_view(), name='SeenBys'),
    path('seen_by/<int:pk>/', SeenBy.View.as_view(), name='SeenBy'),
    path('triggers/', triggers.Views.as_view(), name='triggers'),

]
