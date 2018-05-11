from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic


from ..models.forms import FertilizerForm, CropForm, WeatherConditionForm, TutorialsFrom
from ..models.models import Fertilizer, Crop, Weather, Tutorials
from ..models.voicelabel import Language, VoiceLabel


#add new crop
def add_crop(request):
    if request.method == "POST":
        form = CropForm(request.POST)
        if form.is_valid():
            crop_item = form.save(commit=False)
            crop_item.save()
            return redirect('/vxml/add/crop/')
    else:
        form = CropForm()
    return render(request, 'mamoisson/insert/crop.html', {'crop':form})


