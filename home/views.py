from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'home/index.html', {})

def base_configuracoes(request):
    return render(request, 'home/base_configuracoes.html', {})

def base_aplicar_dinamica(request):
    return render(request, 'home/base_aplicar_dinamica.html', {})