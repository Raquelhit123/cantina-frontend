from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt # REMOVER DA PRODUÇÃO - USAR EM DEBUG APENAS


# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def cadastrar_usuario(request):
    return render(request, 'cadastrar_usuario.html')

@csrf_exempt  # REMOVER DA PRODUÇÃO - USAR EM DEBUG APENAS
def login_usuario(request):
    return render(request, 'login_usuario.html')

def listar_usuarios(request):
    return render(request, 'listar_usuarios.html')

def painel_usuario(request):
    return render(request, 'painel_usuario.html')

def logout_usuario(request):
    return redirect('home_view')