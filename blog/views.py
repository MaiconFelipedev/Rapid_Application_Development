from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from datetime import datetime

# Create your views here.
def welcome(request):
    return HttpResponse("Bem-vindo ao meu blog!")

def eco (request, texto):
    return HttpResponse(f'Você digitou: {texto}')

def info (request):
    data = {
        'disciplina': 'RAD',
        'framework': 'Django',
        'semestre': '2026.1',
    }
    return JsonResponse(data)

# Coloquei o nome de usuário e email no arquivo de context_processors para que 
# fique disponível em todas as páginas do blog, sem precisar 
# passar o contexto em cada view.
def user (request):
    contexto = {
        'is_logged_in': True,
        'role': 'admin',
        'produtos': [
            {'nome': 'Macarrão', 'preco': 5.99},
            {'nome': 'Arroz', 'preco': 4.99},
            {'nome': 'Feijão', 'preco': 6.99},
            {'nome': 'Sal', 'preco': 2.99}
        ]
    }
    return render(request, 'blog/user.html', contexto)

def home (request):
    return render(request, 'blog/home.html')

def contato (request, fone):
    return render(request, 'blog/contato.html', {'fone': fone})