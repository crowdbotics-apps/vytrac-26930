from icecream import ic
from rest_framework import status

from Functions.TestClass import TestClass



class PatientsAppTests(TestClass):

    def test_dieses(self):
        res = self.client.get('/users/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        ic(res.data)
        # TODO
        # assert res.data['Disease']

    def test_sytmptoms_history(self):
        # sym = Symptom.objects.create(name='CMD')
        # sym2 = Symptom.objects.create(name='Coughing')
        # syteomps = SymptomsHistory.objects.create(user=self.user)
        # syteomps.symptoms.add(sym)
        # syteomps.symptoms.add(sym2)
        # syteomps.save()
        # assert self.user.id == 1
        # assert self.user.is_superuser
        #
        # res = self.client.get('/users/1/')
        # self.assertEqual(res.status_code, status.HTTP_200_OK)
        # assert res.data['symptoms_history'][0]['symptoms'][0] == 'CMD'
        # assert res.data['symptoms_history'][0]['symptoms'][1] == 'Coughing'
        res = self.client.get('/users/')
        # print(res.data)
