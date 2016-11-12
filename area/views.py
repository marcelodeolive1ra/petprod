from django.shortcuts import render
from area.models import Area
from django.http import HttpResponseRedirect
from area.forms import Area_Form
from django.shortcuts import get_object_or_404

def area_index(request):
    areas = Area.objects.order_by('id')
    return render(request, 'area/area_index.html', {'areas':areas})

def area_edit(request, id):
    area = get_object_or_404(Area, pk=id)
    form = Area_Form(instance=area)

    if request.method == 'POST':
        form = Area_Form(request.POST, instance=area)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/area')

    return render(request, 'area/area_edit.html', {'form': form, 'id': id})

def area_delete(request, id):
    get_object_or_404(Area, pk=id).delete()
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
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/area')
        else:
            return render(request, 'area/area_new.html', {'form': form, 'id': id})
    else:
        form = Area_Form()
        return render(request, 'area/area_new.html', {'form': form, 'id': id})
