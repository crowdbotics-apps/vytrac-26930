from channels.db import database_sync_to_async
from django.core.asgi import get_asgi_application
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vytrac_26930.settings')
django_asgi_app = get_asgi_application()

from channels.routing import ProtocolTypeRouter, URLRouter
from Functions.get_user import get_user
from Alerts.routing import websocket_urlpatterns

from icecream import ic

from users.models import User


# from jwt import decode


# TODO encode and decode the jwt_token

from asgiref.sync import sync_to_async
class QueryAuthMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        scope['user'] = await get_user(scope["query_string"])
        return await self.app(scope, receive, send)


application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": QueryAuthMiddleware(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
