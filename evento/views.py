from django.shortcuts import render
from evento.models import Evento
from django.http import HttpResponseRedirect
from evento.forms import Evento_Form
from django.shortcuts import get_object_or_404

def evento_index(request):
    eventos = Evento.objects.order_by('id')
    return render(request, 'evento/evento_index.html', {'eventos':eventos})

def evento_edit(request, id):
    '''modulo = get_object_or_404(Modulo, pk=id)
    form = Modulo_Form(instance=modulo)

    if request.method == 'POST':
        form = Modulo_Form(request.POST, instance=modulo)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/modulo')

    return render(request, 'modulo/modulo_edit.html', {'form': form, 'id': id})'''
    pass

def evento_delete(request, id):
    #get_object_or_404(Modulo, pk=id).delete()
    #return HttpResponseRedirect('/modulo')
    pass

def evento_new(request):
    '''modulo = None
    try:
        modulo = Modulo.objects.latest('id')
    except:
        pass
    if modulo == None:
        id = 1
    else:
        id = modulo.id+1
    if request.method == 'POST':
        form = Modulo_Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/modulo')
        else:
            return render(request, 'modulo/modulo_new.html', {'form': form, 'id': id})
    else:
        form = Modulo_Form()
        return render(request, 'modulo/modulo_new.html', {'form': form, 'id': id})'''
    pass