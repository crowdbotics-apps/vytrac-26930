from icecream import ic
from rest_framework import status

from Functions.TestClass import TestClass
from patients.models.models import CPTcode, Booking
from users.models import Address


class AuthTestings(TestClass):

    def test_adress(self):
        Address.objects.create(user=self.user,home='charles street')
        res = self.client.get('/users/1/')
        assert res.data['address']['home']=='charles street'

    def test_booking(self):
        CPTcode.objects.create(name='cpt_name', code='A.10')
        CPTcode.objects.create(name='cpt_name2', code='A.12')
        x = Booking.objects.create(user=self.user)
        x.cpt.add(1)

        y = Booking.objects.create(user=self.user)
        y.cpt.add(2)
        res = self.client.get('/users/1/')
        assert res.data['booked_services']
        assert res.data['booked_services'][0]['cpt'][0] == 'cpt_name'
        assert res.data['booked_services'][1]['cpt'][0] == 'cpt_name2'
        # TODO
        # assert res.data['booked_services']['cpt'][0] == 'cpt_name2'
        # assert res.data['booked_services']['cpt'][1] == 'cpt_name2'
