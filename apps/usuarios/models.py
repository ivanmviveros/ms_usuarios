from django.db import models

from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    ROLES = (
        ("Administrador", "Administrador"),
        ("Profesor", "Profesor"),
        ("Estudiante", "Estudiante"),
    )

    rol = models.CharField(max_length=50, choices=ROLES)
    imagen_perfil = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.get_full_name()

    class Meta:
        ordering = ['first_name','last_name']

    @staticmethod
    def crear_usuario_inicial():
        total_usuarios = Usuario.objects.all().count()
        if total_usuarios == 0:
            password = "Cedesoft"
            usuario = Usuario.objects.create_user('admin', 'root@gmail.com', password)
            usuario.set_password(password)
            usuario.first_name = 'Administrador'
            usuario.is_superuser = True
            usuario.is_staff = True
            usuario.rol = "Administrador"
            usuario.save()