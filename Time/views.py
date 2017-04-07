from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from Time.models import Time
from Time.forms import Time_Form


# Create your views here.

def Time_index(request):
    times = Time.objects.order_by('id')
    return render(request, 'Time/time_index.html', {'times': times})


def Time_new(request):
    if request.method == 'POST':
        form = Time_Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/Time')

        else:
            return render(request, 'Time/time_new.html', {'form': form, 'id': id})
    else:
        form = Time_Form()
        return render(request, 'Time/time_new.html', {'form': form, 'id': id})

def Time_edit(request, id):
    time = get_object_or_404(Time,pk=id)
    form = Time_Form(instance=time)

    if request.method == 'POST':
        form = Time_Form(request.POST, instance=time)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/Time')

    return render(request, 'Time/time_edit.html', {'form':form, 'id':id})

def Time_delete(request, id):
    get_object_or_404(Time, pk=id).delete()
    return HttpResponseRedirect('/Time')