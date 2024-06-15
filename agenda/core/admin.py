from django.contrib import admin
from core.models import Evento

class EventoAdmin(admin.ModelAdmin):
    list_display = ('Titulo','data_evento','data_criacao')
    list_filter = ('Titulo', )
    

admin.site.register(Evento,EventoAdmin)

# Register your models here.
