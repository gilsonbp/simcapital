from datetime import date

from django.test import TestCase

from apps.capital.models import CapitalUser


class CapitalUserTestCase(TestCase):
    def setUp(self):
        CapitalUser.objects.create(
            email='teste@teste.com',
            name='Teste User',
            cpf='12345678901',
            birth_date='1983-10-31'
        )

    def test_create_user(self):
        """ Testing if you can create a capital user """
        user = CapitalUser.objects.get(email='teste@teste.com')
        self.assertEqual(user.email, 'teste@teste.com')
        self.assertEqual(user.name, 'Teste User')
        self.assertEqual(user.cpf, '12345678901')
        self.assertEqual(user.birth_date, date(year=1983, month=10, day=31))
