import pytz
from icecream import ic
from rest_framework import status

from Functions.TestClass import TestClass
from timesheets.models import Column, Value


class AuthTestings(TestClass):

    def test_get_statstics(self):
        col = Column.objects.create(name='Oxygen', user=self.user)
        Value.objects.create(object_id='1', field_value='96%', column=col)
        Value.objects.create(object_id='2', column=col)
        res = self.client.get('/users/')
        for i in res.data:
            if i['username'] == self.user.username:
                assert i['statistics'][0]['name'] == 'Oxygen'
                assert i['statistics'][0]['values'][0]['object_id'] == '1'
                assert i['statistics'][0]['values'][0]['field_value'] == '96%'

    # def test_get_patients(self):
    #     res = self.client.get('/users/?groups__containse=patient', data={'format': 'json'})
    #     self.register_data['email'] = api.rondomeemail
    #     resonse = self.client.post('users/register/', self.register_data, format='json')
    #
    #     resonse = self.client.post('users/verify_email/', self.register_data, format='json')

    # def test_api_jwt_and_permissions_and_users(self):
    #     assert User.objects.count() == 0
    #     self.client.post(self.register_url, self.register_data, format='json')
    #     assert User.objects.count() == 1
    #     u = User.objects.get(id=1)
    #     u.is_active = False
    #     u.save()
    #     #
    #     res = self.client.post(
    #         self.login_url, self.login_data, format='json')
    #     self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
    #     #
    #     u.is_active = True
    #     u.is_email_verified = True
    #     u.is_role_verified = True
    #     u.save()
    #     #
    #     client = APIClient()
    #     res = client.post(
    #         self.login_url, self.login_data, format='json')
    #     self.assertEqual(res.status_code, status.HTTP_200_OK)
    #     self.assertTrue('access' in res.data)
    #     token = res.data['access']
    #     refresh_token = res.data['refresh']
    #     #
    #     verification_url = '/users/token/verify/'
    #     res = self.client.post(
    #         verification_url, {'token': token}, format='json')
    #     self.assertEqual(res.status_code, status.HTTP_200_OK)
    #     #
    #     res = self.client.post(
    #         verification_url, {'token': 'abc'}, format='json')
    #     self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
    #     #
    def test_is_owner(self):
        self.user.is_superuser = False
        self.user.is_staff = False
        self.user.save()
        #
        res = self.client.get('/users/')
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        assert 'You are not permitted to view user' in str(res.data['permission error'])
        #
        res = self.client.get('/users/1/')
        assert self.user.id == 1
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_address(self):
        res = self.client.get('/users/address')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_availability(self):
        res = self.client.get('/users/availability')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_notes(self):
        res = self.client.get('/users/notes')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_users(self):
        res = self.client.get('/users/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)


    def test_update_user_groups(self):
        res = self.client.get('/groups/all_permissions/?codename=view_user.username_field')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        can_view_username = res.data[0]['id']

        res = self.client.get('/groups/all_permissions/?codename=view_patient')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        can_view_patient = res.data[0]['id']


        params = {
            "name": "providers",
            "permissions": [can_view_patient,can_view_username],
        }
        res = self.client.post('/groups/',params)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        params = {
            "groups": ['providers'],
        }

        res = self.client.put('/users/1/',params)
        assert res.data['groups'] == [1]
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_update_user_groups_typos(self):
        params = {
            "name": "providers",
            "permissions": [],
        }
        res = self.client.post('/groups/',params)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        params = {
            "groups": ['providersx'],
        }

        res = self.client.put('/users/1/',params)
        assert '"providersx" is not found, did you mean' in res.data
        assert 'providers' in res.data
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_queries_lookups(self):
        res = self.client.get('/users/?id=2')
        assert "'id', 1" not in str(res.data)
        assert "'id', 2" in str(res.data)

