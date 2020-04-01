from .models import *
from rest_framework import serializers


class CrearUsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'url', 'first_name', 'last_name', 'username', 'email', 'rol', 'imagen_perfil', 'password')


    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        raise NotImplementedError("Utilizar UsuarioSerializer")



class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'url', 'first_name', 'last_name', 'username', 'email', 'rol', 'imagen_perfil')


    def create(self, validated_data):
        raise NotImplementedError("Utilizar CrearUsuarioSerializer")
