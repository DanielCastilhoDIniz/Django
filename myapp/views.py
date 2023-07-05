from django.shortcuts import render, HttpResponse, redirect
from myapp.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


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
        redirect('/')

@login_required(login_url='/login')
def lista_eventos(request):
    evento = Evento.objects.all()
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)
