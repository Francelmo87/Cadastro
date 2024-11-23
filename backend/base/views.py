from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# def registro(request):
#     template = 'registro.html'
#     if request.method == "GET":
#         return render(request, template)
#     else:
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         senha = request.POST.get('senha')
#
#         user = User.objects.filter(username=username).first()
#         if user:
#             return HttpResponse('Já existe um usuário com esse nome')
#
#         user = User.objects.create_user(username=username, email=email, password=senha)
#         user.save()
#
#         return HttpResponse(username)
#
def index(request):
    template = 'index.html'
    return render(request, template)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'voce está conectado')
            return redirect('base:index')
        else:
            messages.success(request, 'Houve um erro, por favor tente novamente ')
            return redirect('base:login')
    else:
        return render(request, 'login.html', {})


@login_required
def logout_user(request):
    logout(request)
    messages.success(request, 'você saiu da aplicação')
    return redirect('base:index')