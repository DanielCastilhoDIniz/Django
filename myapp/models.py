from django.db import models
from django.contrib.auth.models import User

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_do_evento = models.DateTimeField(verbose_name='Data da Criação')
    data_da_criacao = models.DateTimeField(auto_now=True, verbose_name='Data da Criação')
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo
