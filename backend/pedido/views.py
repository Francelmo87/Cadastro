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
    obj = Pedido.objects.get(pk=pk, tipo='V')

    if request.method == 'POST':
        action = request.POST.get('action')  
        if action == 'pendente':
            obj.status = 'P'  
            obj.tipo = 'V'  
            obj.save()
        elif action == 'confirmar':
            obj.status = 'A'  # Muda para Pendente
            obj.tipo = 'A'  # Muda para Pendente
            obj.save()
        return HttpResponseRedirect(reverse('pedido:pedido_visitar_list'))

    context = {
        'object': obj,
    }
    return render(request, template_name, context)

###################################################################################
@login_required
def pedido_abastecer_list(request):
    template_name = 'abastecer/pedido_abastecer_list.html'
    objects = PedidoAbastecer.objects.filter(tipo='A')
    context = {
        'object_list': objects,
        'titulo': 'a abastecer',
        'url_add': 'pedido:pedido_list_all'
    }
    return render(request, template_name, context)

@login_required
def pedido_abastecer_detail(request, pk):
    template_name = 'abastecer/pedido_abastecer_detail.html'
    obj = Pedido.objects.get(pk=pk, tipo='A')

    if request.method == 'POST':
        action = request.POST.get('action') 
        if action == 'pendente':
            obj.status = 'P'
            obj.tipo = 'A'
            obj.save()
        elif action == 'confirmar':
            obj.status = 'A' 
            obj.entregue = True 
            obj.save()
        return HttpResponseRedirect(reverse('pedido:pedido_abastecer_list'))

    context = {
        'object': obj,
    }
    return render(request, template_name, context)