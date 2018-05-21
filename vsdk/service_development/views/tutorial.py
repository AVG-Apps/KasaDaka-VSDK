from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic


from ..models.forms import TutorialsFrom
from ..models.models import Tutorials
from ..models.voicelabel import Language


#SHOW OVERVIEW TUTORIALS
def overview_tutorial(request, id=id):
    latest_tutorial_list = Tutorials.objects.all()
    print(latest_tutorial_list)
    context = {'latest_tutorial_list': latest_tutorial_list}
    return render(request, 'mamoisson/overview/tutorial.html', context)

#ADD TUTORIAL
def add_tutorial(request):
    if request.method == "POST":
        form = TutorialsFrom(request.POST)
        if form.is_valid():
            tutorial_item = form.save(commit=False)
            tutorial_item.save()
            return redirect('/vxml/mamoisson/tutorial/add')
    else:
        form = TutorialsFrom()
    return render(request, 'mamoisson/add/tutorial.html', {'tutorial':form})


#EDIT TUTORIAL
def edit_tutorial(request, id=None):
    item = get_object_or_404(Tutorials, id=id)
    form = TutorialsFrom(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('/vxml/mamoisson/tutorial/')
    return render(request, 'mamoisson/edit/tutorial.html', {'tutorial':form})



#DELETE TUTORIAL
def delete_tutorial(request, id=id):
    tutorial = Tutorials.objects.get(pk=id) #get the fertilizer which needed be deleted
    tutorial.delete()
    return redirect('/vxml/mamoisson/tutorial/')