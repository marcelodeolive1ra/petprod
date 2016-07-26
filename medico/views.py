from django.shortcuts import render
from .models import Medico

# Create your views here.
def medico_index(request):
    medicos = Medico.objects.order_by('perfil')
    return render(request, 'medico/medico_index.html', {'medicos':medicos})
