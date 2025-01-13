from django import forms
from .models import Titular


class UsuarioForm(forms.ModelForm):
    dt_validade = forms.DateField(
        label='Data da Validade',
        required=False,
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'type': 'date'
            }),
        input_formats=('%Y-%m-%d',),
    )

    class Meta:
        model = Titular
        fields = '__all__'