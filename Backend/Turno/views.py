from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404, redirect
from .models import Turno
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TurnoSerializer
from .forms import TurnoForm
from .models import Turno, Usuario 

@user_passes_test(lambda u: u.is_staff)
def cambiar_estado(request, turno_id):
    turno = get_object_or_404(Turno, id=turno_id)
    if request.method == 'POST':
        nuevo_estado = request.POST.get('estado')
        turno.estado = nuevo_estado
        usuario_staff = get_object_or_404(Usuario, username=request.user.username)
        turno.staff_usuario = usuario_staff
        turno.save()
        return redirect('listar_turnos')  
    return render(request, 'cambiar_estado.html', {'turno': turno})

def listar_turnos_pendientes(request):
    turnos = Turno.objects.filter(estado='Pendiente').order_by('-hora_creacion_turno')[:5]
    return render(request, 'turnos_pendientes.html', {'turnos': turnos})


@api_view(['GET'])
def listar_Turnos_Creados(request):
    turnos = Turno.objects.all()
    serializer = TurnoSerializer(turnos, many=True)
    return Response(serializer.data)

#CRUD
def crear_turno(request):
    if request.method == 'POST':
        form = TurnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_turnos')
    else:
        form = TurnoForm()
    return render(request, 'turno_form.html', {'form': form})

def listar_turnos(request):
    turnos = Turno.objects.all()
    return render(request, 'turno_list.html', {'turnos': turnos})

def editar_turno(request, turno_id):
    turno = Turno.objects.get(id=turno_id)
    if request.method == 'POST':
        form = TurnoForm(request.POST, instance=turno)
        if form.is_valid():
            form.save()
            return redirect('listar_turnos')
    else:
        form = TurnoForm(instance=turno)
    return render(request, 'turno_form.html', {'form': form})

def eliminar_turno(request, turno_id):
    turno = Turno.objects.get(id=turno_id)
    if request.method == 'POST':
        turno.delete()
        return redirect('listar_turnos')
    return render(request, 'turno_confirm_delete.html', {'turno': turno})
