from icecream import ic
from rest_framework import status

from Functions.TestClass import TestClass
from users.models import Address


class AuthTestings(TestClass):

    def test_adress(self):
        Address.objects.create(user=self.user,home='charles street')
        res = self.client.get('/users/1/')
        assert res.data['address']['home']=='charles street'