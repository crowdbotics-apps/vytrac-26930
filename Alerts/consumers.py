import json
from urllib.parse import parse_qs

from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from django.db.models.signals import post_save
from django.dispatch import receiver
from icecream import ic
from rest_framework import serializers

from Alerts.models import Alert
from Functions.get_user import get_user
from Functions.queryset_filtering import queryset_filtering


# from Alerts.models import Alert
from users.models import User


class AlertsSer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = '__all__'
from asgiref.sync import sync_to_async, async_to_sync


class AlertsChannle(WebsocketConsumer):

    def connect(self):
        user = self.scope.get('user')
        self.accept()
        ic(self.scope.get('user'))

        try:
            self.send(user.username + ' is connected.')
        except:
            self.send(user + ' is not alowed please provide a valide token')
            # self.disconnect() #TODO
        #
        queries = self.scope['query_string']
        queries = parse_qs(queries.decode("utf8"))
        for i in queries.keys():
            queries[i] = queries[i][0]

        # if user:
        #     if not user.is_staff or not user.is_superuser:
        #         users = users.filter(id=user.id)
        # alerts = queryset_filtering(Alert, queries)
        serializer = AlertsSer(Alert.objects.all(), many=True)
        ic(serializer.data)
        self.send(json.dumps(serializer.data))

        @receiver(post_save, sender=Alert)
        def __init__(sender, created, instance, **kwargs):
            if created:
                serializer = AlertsSer(Alert.objects.get(id=instance.id), many=False)
                self.send(json.dumps(serializer.data))

    def receive(self, text_data):
        errors = []
        user = self.scope.get('user')
        # data = json.loads(text_data)
        # TODO date= Date.objects.get(id=data.id)
        # date = date.seen_by.add(user)
        # notifcation = return_notifcations(self.scope)
        # self.send(notifcation)

        # notifcation = return_notifcations(self.scope)

    def disconnect(self, close_code):
        print(close_code)
        print(self)
