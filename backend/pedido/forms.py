from django import forms

from backend.usuarios.models import Titular

from .models import Pedido


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'


class PedidoVisitarForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'
        exclude = ['entregue']


class PedidoAbastecerForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'
        exclude = ['status']