from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Rodada
from rodada.forms import Rodada_Form

#from django.contrib.auth.decorators import login_required

# Create your views here.
def rodada_index(request):
    rodadas = Rodada.objects.order_by('numeroRodada')
    return render(request, 'rodada/rodada_index.html', {'rodadas':rodadas})

#@login_required(login_url='/adm/login/')
def rodada_new(request):
    # rodada = None
    # try:
    #     rodada = Rodada.objects.latest('numeroRodada')
    # except:
    #     pass
    # if rodada == None:
    #     numeroRodada = 1
    # else:
    #     numeroRodada = rodada.numeroRodada + 1

    if request.method == 'POST':
        form = Rodada_Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rodada')
        else:
            return render(request, 'rodada/rodada_new.html', {'form':form})
    else:
        form = Rodada_Form()
        return render(request, 'rodada/rodada_new.html', {'form': form})

#@login_required(login_url='/adm/login/')
def rodada_edit(request, id):
    rodada = get_object_or_404(Rodada,pk=id)
    form = Rodada_Form(instance=rodada)

    if request.method == 'POST':
        form = Rodada_Form(request.POST, instance=rodada)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rodada')

    return render(request, 'rodada/rodada_edit.html', {'form':form})

