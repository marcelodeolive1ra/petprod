from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from modulo.models import Modulo
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from modulo.forms import Modulo_Form
from django.shortcuts import get_object_or_404

def modulo_index(request):
    modulos = Modulo.objects.order_by('codigo')
    return render(request, 'modulo/modulo_index.html', {'modulos':modulos})

def modulo_edit(request, codigo):
    modulo = get_object_or_404(Modulo, pk=codigo)
    form = Modulo_Form(instance=modulo)

    if request.method == 'POST':
        form = Modulo_Form(request.POST, instance=modulo)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/modulo')

    return render(request, 'modulo/modulo_edit.html', {'form': form, 'codigo': codigo})

def modulo_delete(request, codigo):
    get_object_or_404(Modulo, pk=codigo).delete()
    return HttpResponseRedirect('/modulo')

def modulo_new(request):
    modulo = None
    try:
        modulo = Modulo.objects.latest('codigo')
    except:
        pass
    if modulo == None:
        codigo = 1
    else:
        codigo = modulo.codigo+1
    if request.method == 'POST':
        form = Modulo_Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/modulo')
        else:
            return render(request, 'modulo/modulo_new.html', {'form': form, 'codigo': codigo})
    else:
        form = Modulo_Form()
        return render(request, 'modulo/modulo_new.html', {'form': form, 'codigo': codigo})