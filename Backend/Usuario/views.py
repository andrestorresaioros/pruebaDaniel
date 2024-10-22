from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from .models import Usuario
from .forms import UsuarioForm
from django.shortcuts import render

class ValidarUsuarioView(APIView):
    def get(self, request, numero_identificacion):
        try:
            usuario = Usuario.objects.get(numero_identificacion=numero_identificacion)
            return Response({'exists': True})
        except Usuario.DoesNotExist:
            return Response({'exists': False})

class ListarUsuariosAnonimosView(ListView):
    model = Usuario
    template_name = 'usuario_list_anonimo.html'
    context_object_name = 'usuarios'

class ListarUsuariosView(ListView):
    model = Usuario
    template_name = 'usuario_list.html'
    context_object_name = 'usuarios'

class CrearUsuarioView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuario_form.html'
    success_url = reverse_lazy('listar_usuarios')

class EditarUsuarioView(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuario_form.html'
    success_url = reverse_lazy('listar_usuarios')

class EliminarUsuarioView(DeleteView):
    model = Usuario
    template_name = 'usuario_confirm_delete.html'
    success_url = reverse_lazy('listar_usuarios')
