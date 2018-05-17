from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic


from ..models.forms import FertilizerForm
from ..models.models import Fertilizer
from ..models.voicelabel import Language

#SHOW OVERVIEW FERTILIZERS
def overview_fertilizer(request, id=id):
    latest_fertilizer_list = Fertilizer.objects.all()
    context = {'latest_fertilizer_list': latest_fertilizer_list}
    return render(request, 'mamoisson/overview/fertilizer.html', context)


#ADD FERTILIZER
def add_fertilizer(request):
    if request.method == "POST":
        form = FertilizerForm(request.POST)
        if form.is_valid():
            fertilizer_item = form.save(commit=False)
            fertilizer_item.save()
            return redirect('/vxml/mamoisson/fertilizer/')
    else:
        form = FertilizerForm()
    return render(request, 'mamoisson/add/fertilizer.html', {'fertilizer':form})


#EDIT FERTILIZER
def edit_fertilizer(request, id=None):
    item = get_object_or_404(Fertilizer, id=id)
    form = FertilizerForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('/vxml/mamoisson/fertilizer/')
    return render(request, 'mamoisson/edit/fertilizer.html', {'fertilizer':form})


#DELETE FERTILIZER
def delete_fertilizer(request, id=id):
    fertilizer = Fertilizer.objects.get(pk=id) #get the fertilizer which needed be deleted
    fertilizer.delete()
    return redirect('/vxml/mamoisson/fertilizer/')