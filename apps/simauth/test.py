from django.test import TestCase
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
