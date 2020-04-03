from django.conf import settings
from django.http import JsonResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django_microservices.utilities import login
from rest_framework.decorators import api_view
from rest_framework.exceptions import PermissionDenied
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from rest_framework import viewsets, generics
from .serializers import *

from django.shortcuts import get_object_or_404

class ListarCrearUsuarioViewSet(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Usuario.objects.all()
    serializer_class = CrearUsuarioSerializer


    def get_queryset(self):
        queryset = super().get_queryset()
        try:
            usuario_pk = self.request.META.get(settings.DJANGO_HEADER_MICROSERVICE_USER_PK, 0) or self.request.session[settings.MICROSERVICE_USER_PK_SESSION_KEY]
            usuario = get_object_or_404(Usuario, id=usuario_pk)
            if usuario.rol == "Profesor":
                queryset = queryset.filter(rol="Estudiante")
            elif usuario.rol != "Administrador":
                raise PermissionDenied({})
        except Exception as e:
            raise PermissionDenied({})

        return queryset

class ObtenerModificarUsuarioViewSet(generics.RetrieveUpdateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        usuario_pk = self.request.META.get(settings.DJANGO_HEADER_MICROSERVICE_USER_PK)
        # if usuario_pk is None or usuario_pk == 'None':
        #     raise PermissionDenied({})

        # usuario = get_object_or_404(Usuario, id=int(usuario_pk))
        # if usuario.rol != "Administrador" and instance!=usuario:
        #     raise PermissionDenied({})
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        usuario_pk = self.request.META.get(settings.DJANGO_HEADER_MICROSERVICE_USER_PK)
        if usuario_pk is None or usuario_pk == 'None':
            raise PermissionDenied({})

        usuario = get_object_or_404(Usuario, id=int(usuario_pk))
        if usuario.rol != "Administrador" and instance!=usuario:
            raise PermissionDenied({})
        return self.update(request, *args, **kwargs)

class AutenticarUsuario(APIView):
    def post(self, request, format=None):
        respuesta = {}
        status_code = status.HTTP_200_OK
        try:
            usuario = Usuario.objects.get(username=request.data.get('username', None))
            if usuario.check_password(request.data.get('password', None)):
                respuesta['id'] = usuario.pk
                respuesta[settings.MICROSERVICE_USER_PK_SESSION_KEY] = usuario.pk
                login(request,respuesta)
            else:
                status_code = status.HTTP_404_NOT_FOUND
                respuesta['mensaje'] = "Nombre de usuario o contraseña incorrectos"
            print(request.session[settings.MICROSERVICE_USER_PK_SESSION_KEY])
        except Usuario.DoesNotExist:
            status_code = status.HTTP_404_NOT_FOUND
            respuesta['mensaje'] = "Nombre de usuario o contraseña incorrectos"

        return Response(respuesta, status=status_code)

