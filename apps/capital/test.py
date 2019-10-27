from datetime import date
from decimal import Decimal

from django.test import TestCase

from apps.capital.models import CapitalUser, Salary


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


class SalaryTestCase(TestCase):
    def setUp(self):
        user = CapitalUser.objects.create(
            email='teste@teste.com',
            name='Teste User',
            cpf='12345678901',
            birth_date='1983-10-31'
        )
        Salary.objects.create(
            capital_user=user,
            salary_date=date.today(),
            salary_value=Decimal('2500.12'),
            salary_discount=Decimal('100.12'),
        )

    def test_create_salary(self):
        """ Testing if you can create a capital user """
        salary = Salary.objects.get(
            capital_user__email='teste@teste.com',
            salary_date=date.today()
        )
        self.assertEqual(salary.salary_value, Decimal('2500.12'))
        self.assertEqual(salary.salary_discount, Decimal('100.12'))
