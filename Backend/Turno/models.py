from django.db import models
from django.db.models import Max
from Usuario.models import Usuario
from django.contrib.auth import get_user_model
from django.contrib import admin

class Turno(models.Model):
    ESTADO_TURNO = [
        ('Pendiente', 'Pendiente'),
        ('Activo', 'Activo'),
        ('Finalizado', 'Finalizado'),
    ]
    id = models.AutoField(primary_key=True)
    numero_Turno = models.IntegerField(default=0)
    hora_creacion_turno = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices=ESTADO_TURNO, default='Pendiente')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='turnos')
    staff_usuario = models.ForeignKey(Usuario, null=True, default=1, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # Genera el siguiente número de turno incremental solo si es un nuevo objeto
        if not self.pk:
            max_numero = Turno.objects.aggregate(Max('numero_Turno'))['numero_Turno__max'] or 0
            self.numero_Turno = max_numero + 1
        super().save(*args, **kwargs)

class TurnoAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # Asigna el usuario actual como `staff_usuario`
        if not obj.staff_usuario:
            obj.staff_usuario = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Turno, TurnoAdmin)