from unittest import mock

from asgiref.sync import sync_to_async
from channels.testing import WebsocketCommunicator

from Functions.TestClass import TestClass
from Functions.calendar_setup import calendar_setup
from vytrac_26930.asgi import application

from asgiref.sync import async_to_sync
from django.test import TestCase




class WebsocketTests(TestClass):
    async def test_not_authenticated(self):
        communicator = WebsocketCommunicator(application, "/alerts/")
        connected, subprotocol = await communicator.connect()
        assert connected
        res = await communicator.receive_from()
        assert res == 'connectted'
        res = await communicator.receive_from()
        assert res == 'please provide a token'
        await communicator.disconnect()

    async def test_invalid_token(self):
        communicator = WebsocketCommunicator(application, "/alerts/?token=abc")
        connected, subprotocol = await communicator.connect()
        assert connected
        res = await communicator.receive_from()
        assert res == 'connectted'
        res = await communicator.receive_from()
        assert res == 'token is invalid'
        await communicator.disconnect()

    async def test_invalid_token(self):
        communicator = WebsocketCommunicator(application, f"/alerts/?token={self.token}")
        connected, subprotocol = await communicator.connect()
        assert connected
        res = await communicator.receive_from()
        assert res == 'connectted'
        res = await communicator.receive_from()
        # TODO connect databse for channles testing
        # ic(res)
        # assert res == 'token is invalid'
        await communicator.disconnect()



