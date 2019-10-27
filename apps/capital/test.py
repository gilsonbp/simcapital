from datetime import date, timedelta
from decimal import Decimal

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

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
            salary_value=Decimal('2000.12'),
            salary_discount=Decimal('120.12'),
        )
        Salary.objects.create(
            capital_user=user,
            salary_date=date.today() + timedelta(days=1),
            salary_value=Decimal('3500.15'),
            salary_discount=Decimal('200.12'),
        )
        Salary.objects.create(
            capital_user=user,
            salary_date=date.today() + timedelta(days=2),
            salary_value=Decimal('4600.50'),
            salary_discount=Decimal('300.10'),
        )

    def test_create_salary(self):
        """ Testing if you can create a capital user """
        salary = Salary.objects.get(
            capital_user__email='teste@teste.com',
            salary_date=date.today()
        )
        self.assertEqual(salary.salary_value, Decimal('2000.12'))
        self.assertEqual(salary.salary_discount, Decimal('120.12'))

    def test_average_salary(self):
        user = CapitalUser.objects.get(email='teste@teste.com')
        self.assertEqual(user.get_avg_salary(), Decimal('3366.92'))

    def test_average_discount(self):
        user = CapitalUser.objects.get(email='teste@teste.com')
        self.assertEqual(user.get_avg_discount(), Decimal('206.78'))

    def test_max_salary(self):
        user = CapitalUser.objects.get(email='teste@teste.com')
        self.assertEqual(user.get_max_salary(), Decimal('4600.50'))

    def test_min_salary(self):
        user = CapitalUser.objects.get(email='teste@teste.com')
        self.assertEqual(user.get_min_salary(), Decimal('2000.12'))


class CapitalUserAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = CapitalUser.objects.create(
            email='teste@teste.com',
            name='Teste User',
            cpf='12345678901',
            birth_date='1983-10-31'
        )

    def setUp(self):
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_create_capital_user(self):
        url = reverse('capital:users-list')
        data = {
            "email": "teste1@teste.com",
            "name": "Gilson Paulino",
            "cpf": "12345678901",
            "birth_date": "1983-10-31"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_capital_users(self):
        url = reverse('capital:users-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)

    def test_update_user(self):
        user = CapitalUser.objects.create(
            email='teste2@teste.com',
            name='Teste',
            cpf='12345678902',
            birth_date='1983-10-30'
        )

        url = reverse('capital:users-detail', kwargs={'pk': user.pk})
        data = {
            "name": "Teste User 2",
            "cpf": "00000000000"
        }

        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Teste User 2")
        self.assertEqual(response.data['cpf'], "00000000000")

    def test_delete_user(self):
        user = CapitalUser.objects.create(
            email='teste3@teste.com',
            name='Teste',
            cpf='12345678903',
            birth_date='1983-10-29'
        )

        url = reverse('capital:users-detail', kwargs={'pk': user.pk})

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertIsNone(response.data)


class SalaryAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = CapitalUser.objects.create(
            email='teste4@teste.com',
            name='Teste User',
            cpf='12345678901',
            birth_date='1983-10-31'
        )

    def setUp(self):
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_create_salary(self):
        url = reverse('capital:salaries-list')
        data = {
            "capital_user": self.user.pk,
            "salary_date": "2019-11-02",
            "salary_value": "3050.30",
            "salary_discount": "260.60"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_salaries(self):
        data = {
            "capital_user": self.user,
            "salary_date": "2019-11-02",
            "salary_value": "3050.30",
            "salary_discount": "260.60"
        }
        Salary.objects.create(**data)

        url = reverse('capital:salaries-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
