from datetime import date

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from django.urls import reverse
from .models import Titular, Dependente, Endereco

from .forms import UsuarioForm
from .verificacao import verificar_titulares


@login_required
def titular_list(request):
    template_name = 'titular/titular_list.html'
    titular = Titular.objects.filter()
    # CAMPO DE BUSCA
    search = request.GET.get('search')
    if search:
        titular = titular.filter(nome__icontains=search)
    # Paginação
    paginator = Paginator(titular, 10)
    page_number = request.GET.get('page')
    titular = paginator.get_page(page_number)
    # Verificação se titular continua ativo
    verificar_titulares()
    context = {
        'titular_list': titular
    }
    return render(request, template_name, context)


@login_required
def titular_detail(request, pk):
    template_name = 'titular/titular_detail.html'
    obj = Titular.objects.get(pk=pk)
    context = {
        'object': obj
    }
    return render(request, template_name, context)


@login_required
def titular_add(request):
    template_name = 'titular/titular_add.html'
    form = UsuarioForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('usuarios:titular_list'))
    context = {
        'form': form
    }
    return render(request, template_name, context)


@login_required
def titular_edit(request, pk):
    template_name = 'titular/titular_edit.html'
    obj = Titular.objects.get(pk=pk)
    form = UsuarioForm(request.POST or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('usuarios:titular_list'))
    context = {
        'form': form
    }
    return render(request, template_name, context)


@login_required
def titular_delete(request, pk):
    obj = Titular.objects.get(pk=pk)
    obj.delete()
    return HttpResponseRedirect(reverse('usuarios:titular_list'))


@login_required
def dependente_list(request, pk):
    template_name = 'dependente/dependente_list.html'
    membro = Dependente.objects.filter(titular__pk=pk)
    context = {'dependente_list': membro}
    return render(request, template_name, context)


@login_required
def endereco_titular(request, pk):
    template_name = 'endereco/endereco_titular.html'
    endereco = Endereco.objects.filter(titular__pk=pk)
    context = {'endereco_list': endereco}
    return render(request, template_name, context)
