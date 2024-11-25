from django import forms
from .models import Titular


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Titular
        fields = '__all__'