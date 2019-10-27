from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from apps.simauth.models import User


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('teste@teste.com', 'Teste User')
        User.objects.create_superuser(
            'super@teste.com',
            'Teste Super User',
            '123456'
        )

    def test_create_user(self):
        """ Testing if you can create a user """
        user = User.objects.get(email='teste@teste.com')
        self.assertEqual(user.email, 'teste@teste.com')
        self.assertEqual(user.name, 'Teste User')

    def test_create_superuser(self):
        """ Testing if you can create a superuser """
        user = User.objects.get(email='super@teste.com')
        self.assertEqual(user.email, 'super@teste.com')
        self.assertEqual(user.name, 'Teste Super User')
        self.assertEqual(user.is_superuser, True)


class UserAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            'teste@teste.com',
            'Teste User'
        )
        cls.superuser = User.objects.create_superuser(
            'super@teste.com',
            'Teste Super User',
            '123456'
        )

    def setUp(self):
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_create_user(self):
        url = reverse('simauth:users-list')
        data = {
            "email": "teste1@teste.com",
            "password": "123456",
            "name": "Gilson Paulino",
            "is_superuser": False
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_users(self):
        url = reverse('simauth:users-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 2)

    def test_update_user(self):
        user = User.objects.create_user('teste3@teste.com', 'Teste')

        url = reverse('simauth:users-detail', kwargs={'pk': user.pk})
        data = {
            "name": "Teste User 3",
            "is_superuser": True
        }

        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Teste User 3")
        self.assertEqual(response.data['is_superuser'], True)

    def test_delete_user(self):
        user = User.objects.create_user('teste3@teste.com', 'Teste')

        url = reverse('simauth:users-detail', kwargs={'pk': user.pk})

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertIsNone(response.data)
