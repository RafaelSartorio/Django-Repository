from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime, timedelta
from django.http.response import Http404, JsonResponse

def index(request):
   return redirect('/agenda/')

@login_required(login_url='/login/')
def listaEventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos': evento}
    return render(request, 'agenda.html',dados)

def login_user(request):
    return render(request, 'login.html')

def loginSubmit(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválido")
    return redirect('/')


def logout_user(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def evento(request):
    return render(request, 'eventos.html')

def eventoSubmit(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('Descricao')
        usuario = request.user

        Evento.objects.create(Titulo=titulo,data_evento=data_evento , descricao = descricao , usuario=usuario)
    
    return redirect('/')

@login_required(login_url='/login/')
def deletarEvento(request,id_evento):
    evento = Evento.objects.get(id=id_evento)
    usuario = request.user
    if usuario == evento.usuario:
        evento.delete()
    return redirect('/')





         


