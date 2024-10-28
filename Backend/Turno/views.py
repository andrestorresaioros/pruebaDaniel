from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Turno, Usuario
from .serializers import TurnoSerializer
from .forms import TurnoForm
from django.shortcuts import render

class ValidarTurnoView(APIView):
    def get(self, request, turno_id):
        try:
            turno = Turno.objects.get(id=turno_id)
            return Response({'exists': True})
        except Turno.DoesNotExist:
            return Response({'exists': False})


class CambiarEstadoView(UserPassesTestMixin, View):
    permission_required = 'is_staff'
    template_name = 'cambiar_estado.html'

    def get(self, request, turno_id):
        turno = get_object_or_404(Turno, id=turno_id)
        return render(request, self.template_name, {'turno': turno})

    def post(self, request, turno_id):
        turno = get_object_or_404(Turno, id=turno_id)
        nuevo_estado = request.POST.get('estado')
        turno.estado = nuevo_estado
        usuario_staff = get_object_or_404(Usuario, username=request.user.username)
        turno.staff_usuario = usuario_staff
        turno.save()
        return redirect('listar_turnos')


class ListarTurnosPendientesView(ListView):
    model = Turno
    template_name = 'turnos_pendientes.html'
    context_object_name = 'turnos'

    def get_queryset(self):
        return Turno.objects.filter(estado='Pendiente').order_by('-hora_creacion_turno')[:5]


class ListarTurnosCreadosView(APIView):
    def get(self, request):
        turnos = Turno.objects.all()
        serializer = TurnoSerializer(turnos, many=True)
        return Response(serializer.data)


class CrearTurnoView(CreateView):
    model = Turno
    form_class = TurnoForm
    template_name = 'turno_form.html'
    success_url = reverse_lazy('listar_turnos')


class ListarTurnosView(ListView):
    model = Turno
    template_name = 'turno_list.html'
    context_object_name = 'turnos'


class EditarTurnoView(UpdateView):
    model = Turno
    form_class = TurnoForm
    template_name = 'turno_form.html'
    success_url = reverse_lazy('listar_turnos')

    def get_object(self):
        turno_id = self.kwargs['turno_id']
        return get_object_or_404(Turno, id=turno_id)


class EliminarTurnoView(DeleteView):
    model = Turno
    template_name = 'turno_confirm_delete.html'
    success_url = reverse_lazy('listar_turnos')

    def get_object(self):
        turno_id = self.kwargs['turno_id']
        return get_object_or_404(Turno, id=turno_id)
