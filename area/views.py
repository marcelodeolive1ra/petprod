from django.shortcuts import render
from area.models import Area
from area.models import Area_ClasseSocial
from classe_social.models import Classe_Social
from django.http import HttpResponseRedirect
from area.forms import Area_Form
from area.forms import Area_ClasseSocial_Form
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404

def area_index(request):
    areas = Area.objects.order_by('id')
    area_classe = Area_ClasseSocial.objects.order_by('id')
    return render(request, 'area/area_index.html', {'area_classe':area_classe,'areas':areas})

def area_edit(request, id):
    area = get_object_or_404(Area, pk=id)

    if request.method == 'POST':
        form = Area_Form(request.POST, instance=area)
        form_area_classesocial = Area_ClasseSocial_Form(request.POST)
        classes_sociais = Classe_Social.objects.order_by('id')

        if form.is_valid():
            list_entradas = request.POST.getlist('entrada')
            list_desvios = request.POST.getlist('desvios')
            request.POST = request.POST.copy()
            for entrada in list_entradas:
                request.POST['entrada'] = entrada
                form_area_classesocial = Area_ClasseSocial_Form(request.POST)
                if not form_area_classesocial.is_valid():
                    # retorna o erro, nao consigui fazer o tratamento correto do erro :( sorry. Ele some os campos, mas funciona...
                    return render(request, 'area/area_edit.html',
                                  {'form': form, 'id': id, 'form_area_classesocial': form_area_classesocial,
                                   'classes_sociais': classes_sociais})
            for desvio in list_desvios:
                request.POST['desvios'] = desvio
                form_area_classesocial = Area_ClasseSocial_Form(request.POST)
                if not form_area_classesocial.is_valid():
                    # retorna o erro
                    return render(request, 'area/area_edit.html',
                                  {'form': form, 'id': id,'form_area_classesocial': form_area_classesocial,
                                   'classes_sociais': classes_sociais})

            get_object_or_404(Area, pk=id).delete()
            area = form.save()
            list_entradas = iter(list_entradas)
            list_desvios = iter(list_desvios)
            for classe in Classe_Social.objects.order_by('id'):
                area_classesocial = Area_ClasseSocial(area = area, classe_social=classe, entrada=next(list_entradas), desvios=next(list_desvios))
                area_classesocial.save()

            return HttpResponseRedirect('/area')
        else:
            return render(request, 'area/area_edit.html',
                          {'form': form, 'id': id,
                           'classes_sociais': classes_sociais})

    form = Area_Form(instance=area)
    area_classe = Area_ClasseSocial.objects.order_by('id')
    form_ac = []
    for a in area_classe:
        if a.area_id == int(id):
            ##print("passou aeouuuu uhuuu")
            form_area_classesocial =  Area_ClasseSocial_Form(instance=a)
            form_ac.append(form_area_classesocial)
    classes_sociais = Classe_Social.objects.order_by('id')
    return render(request, 'area/area_edit.html', {'form': form, 'id': id, 'form_ac': form_ac, 'classes_sociais':classes_sociais})


def area_delete(request, id):
    get_object_or_404(Area, pk=id).delete()
    ##get_object_or_404(Area_ClasseSocial, pk=id).delete()
    return HttpResponseRedirect('/area')

def area_new(request):
    area = None
    try:
        area = Area.objects.latest('id')
    except:
        pass
    if area == None:
        id = 1
    else:
        id = area.id+1

    if request.method == 'POST':

        form = Area_Form(request.POST)

        classes_sociais = Classe_Social.objects.order_by('id')
        if form.is_valid():

            list_entradas = request.POST.getlist('entrada')
            list_desvios =  request.POST.getlist('desvios')
            request.POST = request.POST.copy()
            for entrada in list_entradas:
                request.POST['entrada'] = entrada
                form_area_classesocial = Area_ClasseSocial_Form(request.POST)
                if not form_area_classesocial.is_valid():
                        #retorna o erro
                        return render(request, 'area/area_new.html',
                                      {'form': form, 'id': id, 'form_area_classesocial': form_area_classesocial,
                                       'classes_sociais': classes_sociais})
            for desvio in list_desvios:
                request.POST['desvios'] = desvio
                form_area_classesocial = Area_ClasseSocial_Form(request.POST)
                if not form_area_classesocial.is_valid():
                    # retorna o erro
                    return render(request, 'area/area_new.html',
                                  {'form': form, 'id': id, 'form_area_classesocial': form_area_classesocial,
                                   'classes_sociais': classes_sociais})

            area = form.save()
            list_entradas = iter(list_entradas)
            list_desvios = iter(list_desvios)
            for classe in Classe_Social.objects.order_by('id'):
                area_classesocial = Area_ClasseSocial(area=area,classe_social=classe,entrada=next(list_entradas),desvios=next(list_desvios))
                area_classesocial.save()

            return HttpResponseRedirect('/area')
        else:
            form_area_classesocial = Area_ClasseSocial_Form(request.POST)
            return render(request, 'area/area_new.html', {'form': form, 'id': id, 'form_area_classesocial': form_area_classesocial,'classes_sociais':classes_sociais})
    else:
        form = Area_Form()
        form_area_classesocial = Area_ClasseSocial_Form()
        classes_sociais = Classe_Social.objects.order_by('id')
        return render(request, 'area/area_new.html', {'form': form, 'id': id, 'form_area_classesocial': form_area_classesocial, 'classes_sociais':classes_sociais})
