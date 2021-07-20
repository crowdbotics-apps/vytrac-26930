from urllib.parse import parse_qs

from channels.db import database_sync_to_async
from icecream import ic
from rest_framework_simplejwt.tokens import UntypedToken

from users.models import User

@database_sync_to_async
def get_user(querys):
    user_id = None
    token = parse_qs(querys.decode("utf8")).get('token')
    ic(User.objects.count())
    if token:
        token = token[0]
    else:
        return 'please provide a token'

    try:
        token_data = UntypedToken(token)
        user_id = token_data["user_id"]
        ic(user_id)
    except:
        return 'token is invalid'

    try:
        return User.objects.get(id=user_id)
    except User.DoesNotExist:
        return 'AnonymousUser'