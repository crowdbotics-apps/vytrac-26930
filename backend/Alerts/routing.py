from django.conf.urls import url

from .consumers import AlertsChannle
from django.urls import path, re_path

websocket_urlpatterns = [
    re_path('alerts/', AlertsChannle.as_asgi()),
    # path('chat/', Chat.as_asgi())
]
