from django.shortcuts import render, HttpResponse, redirect
from myapp.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# def index(request):
#     return redirect('/agenda/')
def login_user(request):
    return render(request, 'login.html')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "   Usuário ou senha inválido")

    return redirect('/')


def logout_user(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/login')
def lista_eventos(request):
    evento = Evento.objects.all()
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)


@login_required(login_url='/login/')
def evento(request):
    return render(request, 'evento.html')

@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_do_evento = request.POST.get('data_do_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        Evento.objects.create(titulo=titulo,
                              data_do_evento=data_do_evento,
                              descricao=descricao,
                              usuario=usuario)
    return redirect('/')
