from django import forms

from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombres', 'apellidos', 'numero_celular', 'numero_identificacion', 'staff', 'foto']
