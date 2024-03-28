from django.shortcuts import render
from django.http import HttpResponse

from .models import Usuario

def login(request):
    return HttpResponse('login')

def cadastro(request):
    return render(request, 'cadastro.html')

def valida_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    usuario = Usuario(nome=nome, email=email, senha=senha)
    usuario.save()

    return HttpResponse(f'{nome} {email} {senha}')
