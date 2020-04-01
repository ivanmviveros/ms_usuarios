from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('auth', AutenticarUsuario.as_view(), name='usuarios_autenticar'),
    path('', ListarCrearUsuarioViewSet.as_view()),
    path('<int:pk>/', ObtenerModificarUsuarioViewSet.as_view(), name='usuario-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
