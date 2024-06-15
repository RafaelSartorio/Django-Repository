from django.contrib.auth.models import User
from django.db import models

class Evento(models.Model):
    Titulo = models.CharField(max_length=100)
    descricao = models.TextField(null=True , blank=True)
    data_evento= models.DateTimeField(verbose_name='Data do evento')
    data_criacao = models.DateTimeField(auto_now=True, verbose_name='Data de criação')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Evento'

    def __str__(self):
        return self.Titulo
    
    def data_evento_criacao(self):
        return self.data_evento.strftime('%d/%m/%Y as %H:%M hrs')

# Create your models here.
