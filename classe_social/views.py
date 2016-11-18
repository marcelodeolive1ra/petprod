

# Create your views here.
from django.shortcuts import render
from classe_social.models import Classe_Social
from django.http import HttpResponseRedirect
from classe_social.forms import Classe_Social_Form
from django.shortcuts import get_object_or_404

def classe_social_index(request):
    classes = Classe_Social.objects.order_by('id')
    return render(request, 'classe_social/classe_social_index.html', {'classes':classes})

def classe_social_edit(request, id):
    classe = get_object_or_404(Classe_Social, pk=id)
    form = Classe_Social_Form(instance=classe)

    if request.method == 'POST':
        form = Classe_Social_Form(request.POST, instance=classe)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/classe_social')

    return render(request, 'classe_social/classe_social_edit.html', {'form': form, 'id': id})

def classe_social_delete(request, id):
    get_object_or_404(Classe_Social, pk=id).delete()
    return HttpResponseRedirect('/classe_social')

def classe_social_new(request):
    classe = None
    try:
        classe = Classe_Social.objects.latest('id')
    except:
        pass
    if classe == None:
        id = 1
    else:
        id = classe.id+1
    if request.method == 'POST':
        print(request.POST)
        form = Classe_Social_Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/classe_social')
        else:
            return render(request, 'classe_social/classe_social_new.html', {'form': form, 'id': id})
    else:
        form = Classe_Social_Form()
        return render(request, 'classe_social/classe_social_new.html', {'form': form, 'id': id})