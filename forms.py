from django import forms
from .models import Miembro, Membresia # Importa Membresia también si la necesitas en el futuro

class MiembroForm(forms.ModelForm):
    class Meta:
        model = Miembro
        fields = ['nombre', 'apellido', 'fecha_nacimiento', 'telefono', 'id_membresia', 'foto_perfil']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }