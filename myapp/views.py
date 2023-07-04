from django.shortcuts import render, HttpResponse
from myapp.models import Evento


def lista_eventos(request):
    evento = Evento.objects.all()
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)
