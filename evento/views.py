from django.shortcuts import render
from evento.models import Evento
from evento.models import Evento_ModificaEntrada
from django.http import HttpResponseRedirect
from area.models import Area
from area.models import Area_ClasseSocial
from evento.forms import Evento_Form
from evento.forms import Evento_ModificaEntrada_Form
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404

def evento_index(request):
    eventos = Evento.objects.order_by('id')
    modificaEvento = Evento_ModificaEntrada.objects.order_by('evento')
    #evento_modifica = Evento_ModificaEntrada.object.order_by('id')
    return render(request, 'evento/evento_index.html', {'eventos':eventos, 'modificacoes': modificaEvento})

def area_index(request):
    areas = Area.objects.order_by('id')
    area_classe = Area_ClasseSocial.objects.order_by('id')
    return render(request, 'area/area_index.html', {'area_classe':area_classe,'areas':areas})

def evento_edit(request, id):
    print("oi")
'''
    evento = get_object_or_404(Evento, pk=id)

    if request.method == 'POST':
        form = Evento_Form(request.POST, instance=evento)
        form_modifica = Evento_ModificaEntrada_Form(request.POST)
        classes_sociais = Area_ClasseSocial.objects.order_by('id')

        if form.is_valid():
            list_modificadorEntrada = request.POST.getlist('entradaModificada')
            list_modificadorDesvio = request.POST.getlist('desvioModificado')
            request.POST = request.POST.copy()

            for modificadorEntrada in list_modificadorEntrada:
                request.POST['modificadorEntrda'] = modificadorEntrada
                form_evento_modifica = Evento_ModificaEntrada_Form(request.POST)
                if not form_evento_modifica.is_valid():
                    # retorna o erro, nao consigui fazer o tratamento correto do erro :( sorry. Ele some os campos, mas funciona...
                    return render(request, 'evento/evento_edit.html',
                                  {'form': form, 'id': id, 'form_evento_modifica': form_evento_modifica,
                                   'classes_sociais': classes_sociais})
            for modificadorDesvio in list_modificadorDesvio:
                request.POST['modificadorDesvio'] = modificadorDesvio
                form_evento_modifica = Evento_ModificaEntrada_Form(request.POST)
                if not form_evento_modifica.is_valid():
                    # retorna o erro, nao consigui fazer o tratamento correto do erro :( sorry. Ele some os campos, mas funciona...
                    return render(request, 'evento/evento_edit.html',
                                  {'form': form, 'id': id, 'form_evento_modifica': form_evento_modifica,
                                   'classes_sociais': classes_sociais})

            get_object_or_404(Evento, pk=id).delete()
            evento = form.save()
            list_modificadorEntrada= iter(list_modificadorEntrada)
            list_modificadorDesvio = iter(list_modificadorDesvio)

            for classe in Area_ClasseSocial.objects.order_by('id'):
                evento_modificaentrada = Evento_ModificaEntrada(evento = evento, classe_social=classe, modificadorEntrada=next(list_modificadorEntrada), modificadorDesvio=next(list_modificadorDesvio))
                evento_modificaentrada.save()

            return HttpResponseRedirect('/evento')
        else:
            return render(request, 'evento/evento_edit.html',
                              {'form': form, 'id': id,
                               'classes_sociais': classes_sociais})

    form = Evento_Form(instance=evento)
    evento_modificaentrada =  Evento_ModificaEntrada.objects.order_by('id')
    form_ac = []
    for e in evento_modificaentrada:
        if e.evento_id == int(id):
            ##print("passou aeouuuu uhuuu")
            form_evento_modifica = Evento_ModificaEntrada_Form(instance=e)
            form_ac.append(form_evento_modifica)
    area_classes_sociais = Area_ClasseSocial.objects.order_by('id')
    return render(request, 'area/area_edit.html',
                  {'form': form, 'id': id, 'form_ac': form_ac, 'classes_sociais': area_classes_sociais})

'''
def evento_delete(request, id):
    '''    #get_object_or_404(Modulo, pk=id).delete()
    #return HttpResponseRedirect('/modulo')
    pass
'''

def evento_new(request):
    evento = None
    try:
        evento = Evento.objects.latest('id')
    except:
        pass
    if evento == None:
        id = 1
    else:
        id = evento.id+1

    if request.method == 'POST':

        form = Evento_Form(request.POST)

        area_classe_sociais = Area_ClasseSocial.objects.order_by('area')


        list_modificadorentradas = request.POST.getlist('modificadorEntrada')
        list_modificadordesvios =  request.POST.getlist('modificadorDesvio')


        request.POST = request.POST.copy()


        form_em = [] #form_evento_modifica
        list = []


        for i in range(0, len(list_modificadorentradas)):
            form_evento_modificaentrada = Evento_ModificaEntrada_Form(initial={'modificadorEntrada': list_modificadorentradas[i], 'modificadorDesvio': list_modificadordesvios[i]})
            form_em.append(form_evento_modificaentrada)

        if form.is_valid():
            for modificadorEntrada in list_modificadorentradas:
                request.POST['modificadorEntrada'] = modificadorEntrada
                form_evento_modificaentrada = Evento_ModificaEntrada_Form(request.POST)
                if not form_evento_modificaentrada.is_valid():
                        #retorna o erro
                        return render(request, 'evento/evento_edit.html',
                                      {'form': form, 'id': id, 'area_classe_sociais': area_classe_sociais,
                                       'form_evento_modificaentrada': form_evento_modificaentrada, 'list': list})
            for modificadorDesvio in list_modificadordesvios:
                request.POST['modificadorDesvio'] = modificadorDesvio
                form_evento_modificaentrada = Evento_ModificaEntrada_Form(request.POST)
                if not form_evento_modificaentrada.is_valid():
                    # retorna o erro
                    return render(request, 'area/area_edit.html',
                                  {'form': form, 'id': id, 'area_classe_sociais': area_classe_sociais,
                                   'form_evento_modificaentrada': form_evento_modificaentrada, 'list': list})

            evento = form.save()
            list_modificadorentradas = iter(list_modificadorentradas)
            list_modificadordesvios = iter(list_modificadordesvios)



            for area_classe in Area_ClasseSocial.objects.order_by('id'):
                evento_modificaentrada = Evento_ModificaEntrada(evento=evento, area_classe_social=area_classe, modificadorEntrada=next(list_modificadorentradas), modificadorDesvio=next(list_modificadordesvios))
                evento_modificaentrada.save()

            return HttpResponseRedirect('/evento')
        else:
            #form_area_classesocial = Area_ClasseSocial_Form(request.POST)
            return render(request, 'evento/evento_edit.html',
                          {'form': form, 'id': id, 'area_classes_sociais': area_classe_sociais,
                           'form_evento_modificaentrada': form_evento_modificaentrada, 'list': list})
    else:
        form = Evento_Form()
        area_classes_social = Area_ClasseSocial.objects.order_by('id')
        form_em = []
        nomesArea = []
        nomesClasses = []
        for a in area_classes_social:
            form_evento_modificaentrada = Evento_ModificaEntrada_Form()
            form_em.append(form_evento_modificaentrada)
            nomesArea.append(a.area.nome)
            nomesClasses.append(a.classe_social.nome)
        list = zip(form_em, nomesArea, nomesClasses)
        return render(request, 'evento/evento_new.html', {'form': form, 'id': id, 'area_classes_social': area_classes_social, 'list': list})