from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Medico
from medico.forms import Medico_Form

# Create your views here.
def medico_index(request):
    medicos = Medico.objects.order_by('perfil')
    return render(request, 'medico/medico_index.html', {'medicos':medicos})

def medico_new(request):
    medico = Medico.objects.latest('id')
    id = medico.id+1
    if request.method == 'POST':
        form = Medico_Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/medico')
        else:
            return render(request, 'medico/medico_new.html', {'form':form, 'id':id})
    else:
        form = Medico_Form()
        return render(request, 'medico/medico_new.html', {'form': form, 'id':id})
