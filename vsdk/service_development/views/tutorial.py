from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic


from ..models.forms import TutorialsFrom
from ..models.models import Tutorials
from ..models.voicelabel import Language


#add new tutorial
def add_tutorial(request):
    if request.method == "POST":
        form = TutorialsFrom(request.POST)
        if form.is_valid():
            tutorial_item = form.save(commit=False)
            tutorial_item.save()
            return redirect('/vxml/add/tutorial/')
    else:
        form = TutorialsFrom()
    return render(request, 'mamoisson/add/tutorial.html', {'tutorial':form})
