from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Usuario
from django.shortcuts import render, redirect
from .forms import UsuarioForm

@api_view(['GET'])
def validar_usuario(request, numero_identificacion):
    try:
        usuario = Usuario.objects.get(numero_identificacion=numero_identificacion)
        return Response({'exists': True})
    except Usuario.DoesNotExist:
        return Response({'exists': False})

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario_list.html', {'usuarios': usuarios})


#CRUD
def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            # Aquí se crea el usuario
            nuevo_usuario = form.save(commit=False)
            nuevo_usuario.save()
            return redirect('listar_usuarios')  # Redirige a la lista de usuarios después de crear
    else:
        form = UsuarioForm()
    return render(request, 'usuario_form.html', {'form': form})

def editar_usuario(request, usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuario_form.html', {'form': form})

def eliminar_usuario(request, usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('listar_usuarios')
    return render(request, 'usuario_confirm_delete.html', {'usuario': usuario})
