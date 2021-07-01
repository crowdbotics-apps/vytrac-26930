from urllib.parse import parse_qs

from channels.db import database_sync_to_async
from icecream import ic
from rest_framework_simplejwt.tokens import UntypedToken

from users.models import User
from django.core.exceptions import ValidationError

@database_sync_to_async
def get_user(querys):
    ic(User.objects.count())

    try:
        token = parse_qs(querys.decode("utf8"))['token'][0]
        token_data = UntypedToken(token)
        user_id = token_data["user_id"]
    except:
        return 'token is invalid'

    try:
        return User.objects.get(id=user_id)
    except User.DoesNotExist:
        return 'AnonymousUser'