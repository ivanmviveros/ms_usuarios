from django.test import TestCase

# Create your tests here.
from apps.usuarios.models import Usuario


class UserTestCase(TestCase):
    def setUp(self):
        Usuario.crear_usuario_inicial()

    def test_initial_user_is_superuser(self):
        user = Usuario.objects.get(username='admin')
        self.assertEqual(user.is_superuser,True)

    def test_initial_user_is_administrator(self):
        user = Usuario.objects.get(username='admin')
        self.assertEqual(user.rol,"Administrador")