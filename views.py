from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Pedido

@login_required
def pedido_list_all(request):
    template_name = 'pedido_list_all.html'
    objects = Pedido.objects.all()
    context = {
        'object_list': objects,
        'url_add': 'pedido:pedido_add'
    }
    return render(request, template_name, context)
