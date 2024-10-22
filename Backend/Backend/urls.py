"""
URL configuration for Backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from Usuario.views import validar_usuario, listar_usuarios,listar_usuarios_anonimos
from Turno.views import listar_turnos, cambiar_estado, listar_turnos_pendientes
#from Usuario.views import crear_usuario, listar_usuarios, editar_usuario, eliminar_usuario
from Turno.views import crear_turno, listar_turnos, editar_turno, eliminar_turno
from Turno.views import cambiar_estado, listar_Turnos_Creados
from django.conf.urls.static import static
from django.conf import settings
from Usuario.views import ValidarUsuarioView, ListarUsuariosView, ListarUsuariosAnonimosView, CrearUsuarioView, EditarUsuarioView, EliminarUsuarioView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('validar_usuario/<int:numero_identificacion>/', ValidarUsuarioView.as_view(), name='validar_usuario'),
    path('api/turnos/', listar_Turnos_Creados, name='listar_turnos_creados'),

    path('turnos/pendientes/', listar_turnos_pendientes, name='listar_turnos_pendientes'),
    path('turno/cambiar-estado/<int:turno_id>/', cambiar_estado, name='cambiar_estado'),
    path('usuarios_anonimos/', ListarUsuariosAnonimosView.as_view(), name='listar_usuarios_anonimos'),

   
    path('usuarios/', ListarUsuariosView.as_view(), name='listar_usuarios'),
    path('usuarios/crear/', CrearUsuarioView.as_view(), name='crear_usuario'),
    path('usuarios/editar/<int:pk>/', EditarUsuarioView.as_view(), name='editar_usuario'),
    path('usuarios/eliminar/<int:pk>/', EliminarUsuarioView.as_view(), name='eliminar_usuario'),


    path('turnos/', listar_turnos, name='listar_turnos'),
    path('turnos/crear/', crear_turno, name='crear_turno'),
    path('turnos/editar/<int:turno_id>/', editar_turno, name='editar_turno'),
    path('turnos/eliminar/<int:turno_id>/', eliminar_turno, name='eliminar_turno'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)