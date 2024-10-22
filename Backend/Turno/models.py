from django.db import models
from Usuario.models import Usuario

# Create your models here.
class Turno(models.Model):
    ESTADO_TURNO=[
        ('Pendiente', 'Pendiente'),
        ('Activo', 'Activo'),
        ('Finalizado', 'Finalizados'),
    ]
    id= models.AutoField(primary_key=True)
    numero_Turno= models.IntegerField(default=0)
    hora_creacion_turno = models.DateTimeField(auto_now_add=True) 
    estado = models.CharField(max_length=10, choices=ESTADO_TURNO, default='Pendiente')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='turnos')
    staff_usuario = models.ForeignKey(Usuario, null=True, default=1, on_delete=models.CASCADE)  # Cambia 1 al ID de un Usuario existente
