from icecream import ic
from rest_framework import status

from Functions.TestClass import TestClass


class PatientsAppTests(TestClass):

    def test_emergency_contct_link(self):
        res = self.client.get('/patient/emergency_contact/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        # res = self.client.get('/patient/emergency_contact/1/', )
        # self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_patient_relational_data(self):
        res = self.client.post('/patient/',
                               {
                                   "created_by": self.user.id,
                                   "user": self.user2.id,
                               }
                               )
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        res = self.client.post('/patient/emergency_contact/',
                               {
                                   "patient": [1],
                                   "first_name": "Sam",
                                   "relationship": 'siblings',

                               }
                               )
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        # #
        res = self.client.get('/patient/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        emergency_contact = res.data[0]['emergency_contact'][0]
        assert len(emergency_contact) > 1
        assert 'patient' not in str(emergency_contact)

    def test_RPMplan(self):
        res = self.client.get('/patient/RPMplan')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
