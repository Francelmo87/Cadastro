from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse



from .forms import PedidoForm
from .models import Pedido, PedidoVisitar, PedidoAbastecer


@login_required
def pedido_list_all(request):
    template_name = 'pedido_list_all.html'
    objects = Pedido.objects.all()
    context = {
        'object_list': objects,
        'url_add': 'pedido:pedido_add'
    }
    return render(request, template_name, context)


@login_required
def pedido_add(request):
    template_name = 'pedido_add.html'
    form = PedidoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.save()
            return HttpResponseRedirect(reverse('pedido:pedido_list_all'))
    context = {
        'form': form,
        'url_add': 'pedido:pedido_add'
    }
    return render(request, template_name, context)


##########################################################################
@login_required
def pedido_visitar_list(request):
    template_name = 'visitar/pedido_visitar_list.html'
    objects = PedidoVisitar.objects.all()
    context = {
        'object_list': objects,
        'titulo': 'a visitar',
        'url_add': 'pedido:pedido_list_all'
    }
    return render(request, template_name, context)

@login_required
def pedido_visitar_detail(request, pk):
    template_name = 'visitar/pedido_visitar_detail.html'
    obj = Pedido.objects.get(pk=pk)

    if request.method == 'POST':
        action = request.POST.get('action')  # Identifica a ação desejada
        if action == 'confirmar' and obj.status == 'V' or 'P':
            obj.status = 'A'  # Muda para Aprovado
            obj.save()
        elif action == 'pendente' and obj.status == 'V':
            obj.status = 'P'  # Muda para Pendente
            obj.save()
        return HttpResponseRedirect(reverse('pedido:pedido_visitar_list'))

    context = {
        'object': obj,
        'url_add': 'pedido:visitar/pedido_list_all'
    }
    return render(request, template_name, context)

###################################################################################
@login_required
def pedido_abastecer_list(request):
    template_name = 'abastecer/pedido_abastecer_list.html'
    objects = PedidoAbastecer.objects.all()
    context = {
        'object_list': objects,
        'titulo': 'a abastecer',
        'url_add': 'pedido:pedido_list_all'
    }
    return render(request, template_name, context)