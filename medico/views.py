from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Medico
from medico.forms import Medico_Form

#from django.contrib.auth.decorators import login_required

# Create your views here.
def medico_index(request):
    medicos = Medico.objects.order_by('perfil')
    return render(request, 'medico/medico_index.html', {'medicos':medicos})

#@login_required(login_url='/adm/login/')
def medico_new(request):
    medico = None
    try:
        medico = Medico.objects.latest('id')
    except:
        pass
    if medico == None:
        id = 1
    else:
        id = medico.id + 1

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

#@login_required(login_url='/adm/login/')
def medico_edit(request, id):
    medico = get_object_or_404(Medico,pk=id)
    form = Medico_Form(instance=medico)

    if request.method == 'POST':
        form = Medico_Form(request.POST, instance=medico)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/medico')

    return render(request, 'medico/medico_edit.html', {'form':form, 'id':id})

#@login_required(login_url='/adm/login/')
def medico_delete(request, id):
    get_object_or_404(Medico, pk=id).delete()
    return HttpResponseRedirect('/medico')