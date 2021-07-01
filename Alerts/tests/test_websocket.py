# from users.models import User
import pytest
from asgiref.sync import async_to_sync, sync_to_async
from channels.testing import WebsocketCommunicator
from icecream import ic

# from Alerts.consumers import AlertsChannle
# from Alerts.models import Alert
# import asyncio
from Functions.TestClass import TestClass
from users.models import User
from vytrac_26930.asgi import application


class WebsocketTests(TestClass):

    async def test_connect(self):
        communicator = WebsocketCommunicator(application, '/alerts/')
        connected, subprotocol = await communicator.connect()
        assert connected
        res = await communicator.receive_from()
        ic(res)

        await communicator.disconnect()

    async def test_connect(self):
        communicator = WebsocketCommunicator(application, f'alerts/?token={self.token}')
        connected, subprotocol = await communicator.connect()
        assert connected
        await communicator.disconnect()




    # async def test_not_authenticated(self):
    #     uri = f'ws://localhost:8000/alerts/'
    #     async with websockets.connect(uri) as websocket:
    #         res = await websocket.recv()
    #         assert 'token is invalid' in res
    #         try:
    #             res = await websocket.recv()
    #         except:
    #             res = None
    #         assert res == None
    #
    # async def test_recies_alerts(self):
    #     async with websockets.connect(self.url) as websocket:
    #         res = await websocket.recv()
    #         ic(res)

    # async def test_connect(self):
    #     uri = f'ws://localhost:8000/alerts/?token={self.token2}&fields=username'
    #     async with websockets.connect(uri) as websocket:
    #         res = await websocket.recv()
    #         assert res
    # websocket.disconnect()

    # async def test_send(self):
    #     uri = f'ws://localhost:8000/alerts/?token={self.token2}&fields=username'
    #     async with websockets.connect(uri) as websocket:
    #         message = {"":""}
    #         res = await websocket.send('message')

    # async def test_is_auth(self):
    #     uri = f'ws://localhost:8000/alerts/?token={self.token}&x=xxx'
    #     async with websockets.connect(uri) as websocket:
    #         res = await websocket.recv()
    #         res = json.loads(res)
    # TODO
    # assert self.all_dates == len(res)

    # async def test_can_see_only_own_data(self):
    #     uri = f'ws://localhost:8000/alerts/?token={self.token3}'
    #     async with websockets.connect(uri) as websocket:
    #         res = await websocket.recv()
    #         res = json.loads(res)

    # TODO
    # self.assertEqual(len(res), 1)

    # async def test_fields_filter(self):
    #     uri = f'ws://localhost:8000/alerts/?token={self.token2}&fields=username'
    #     async with websockets.connect(uri) as websocket:
    #         res = await websocket.recv()
    #         res = json.loads(res)
    # TODO
    # for i in res:

    #             assert 'username' in i
    #             assert 'events' not in i

    # async def test_live_update(self):
    #     uri = f'ws://localhost:8000/alerts/?token={self.token}'
    #     async with websockets.connect(uri) as websocket:
    #         res = await websocket.recv()
    #         res = json.loads(res)
    # P_res = sync_to_async(self.client.post)('/calendars/', {
    #     "title": "first",
    #     "description": "",
    #     "start": self.after_1_d,
    #     "end": self.after_3_d,
    #     "from_time": self.after_1_h,
    #     "to_time": self.after_5_h,
    #     "created_by": 1,
    #     "date_type": 1,
    #     "users": [1],
    #     "recurrence": [
    #         "1 sunday",
    #     ],
    # })
    # self.assertEqual(P_res.status_code, status.HTTP_201_CREATED)

    # async def test_queries(self):
    #     uri = f'ws://localhost:8000/alerts/?token={self.token}&events__title=ddd'
    #     async with websockets.connect(uri) as websocket:
    #         res = await websocket.recv()
    #         res = json.loads(res)



            # assert 'token is invalid' in res

    # assert self.all_dates == len(res)

    # async def test_can_see_only_own_data(self):
    #     uri = f'ws://localhost:8000/alerts/?token={self.token3}'
    #     async with websockets.connect(uri) as websocket:
    #         res = await websocket.recv()
    #         res = json.loads(res)

    # TODO
    # self.assertEqual(len(res), 1)

    # async def test_fields_filter(self):
    #     uri = f'ws://localhost:8000/alerts/?token={self.token2}&fields=username'
    #     async with websockets.connect(uri) as websocket:
    #         res = await websocket.recv()
    #         res = json.loads(res)
    # TODO
    # for i in res:

    #             assert 'username' in i
    #             assert 'events' not in i

    # async def test_live_update(self):
    #     uri = f'ws://localhost:8000/alerts/?token={self.token}'
    #     async with websockets.connect(uri) as websocket:
    #         res = await websocket.recv()
    #         res = json.loads(res)
    # P_res = sync_to_async(self.client.post)('/calendars/', {
    #     "title": "first",
    #     "description": "",
    #     "start": self.after_1_d,
    #     "end": self.after_3_d,
    #     "from_time": self.after_1_h,
    #     "to_time": self.after_5_h,
    #     "created_by": 1,
    #     "date_type": 1,
    #     "users": [1],
    #     "recurrence": [
    #         "1 sunday",
    #     ],
    # })
    # self.assertEqual(P_res.status_code, status.HTTP_201_CREATED)

    # async def test_queries(self):
    #     uri = f'ws://localhost:8000/alerts/?token={self.token}&events__title=ddd'
    #     async with websockets.connect(uri) as websocket:
    #         res = await websocket.recv()
    #         res = json.loads(res)
    # TODO

    # def _create_data(self):
    #     pass
    # def _create_events(self):
    #     pass
    # def tearDown(self):
        # destroy_data
    # TODO
    # async def test_connect(self):
    #     uri = f'ws://localhost:8000/alerts/?token={self.token2}&fields=username'
    #     async with websockets.connect(uri) as websocket:
    #         res = await websocket.recv()
    #         assert res
            # websocket.disconnect()


    # async def test_send(self):
    #     uri = f'ws://localhost:8000/alerts/?token={self.token2}&fields=username'
    #     async with websockets.connect(uri) as websocket:
    #         message = {"":""}
    #         res = await websocket.send('message')

    # @pytest.mark.asyncio
    async def test_connect(self):
        communicator = WebsocketCommunicator(application, f'alerts/?token={self.token}')
        connected, subprotocol = await communicator.connect()
        assert connected
        await communicator.disconnect()