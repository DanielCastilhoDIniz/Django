from django.contrib import admin
from myapp.models import Evento

# Register your models here.


class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_do_evento', 'data_da_criacao')
    list_filter =('titulo','usuario',)


admin.site.register(Evento, EventoAdmin)
