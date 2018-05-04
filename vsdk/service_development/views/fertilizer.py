from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from ..models.forms import FertilizerForm, CropForm, WeatherConditionForm
from ..models.models import Fertilizer

from . import base

#Render the Index page
def main_page(request):
    latest_fertilizer_list = Fertilizer.objects.all()
    context = {'latest_fertilizer_list': latest_fertilizer_list}
    return render(request, 'fertilizer_website/main_page.html', context)

#Render the Fertilizer page
def fertilizer(request, id=id):
    fertilizer = Fertilizer.objects.get(id=id)
    return render(request, 'fertilizer_website/detail.html', {'fertilizer': fertilizer})


#Render the voice XML application
def voice_app(request):
    latest_fertilizer_list = Fertilizer.objects.all()
    context = {'latest_fertilizer_list': latest_fertilizer_list}
    return render(request, 'main-en.xml', context,  content_type='text/xml')


#add new fertilizer to the the index page
def add_fertilizer(request):
    if request.method == "POST":
        form = FertilizerForm(request.POST)
        if form.is_valid():
            fertilizer_item = form.save(commit=False)
            fertilizer_item.save()
            return redirect('/vxml/fertilizer/' + str(fertilizer_item.id) + '/')
    else:
        form = FertilizerForm()
    return render(request, 'fertilizer_website/fertilizer_form.html', {'form':form})

#edit the fertilizer on the detail page
def edit_fertilizer(request, id=None):
    item = get_object_or_404(Fertilizer, id=id)
    form = FertilizerForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('/vxml/fertilizer/' + str(item.id) + '/')
    return render(request, 'fertilizer_website/fertilizer_form.html', {'form':form})

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
    return render(request, 'fertilizer_website/crop_form.html', {'form':form})


#add new weather
def add_weather(request):
    if request.method == "POST":
        form = WeatherConditionForm(request.POST)
        if form.is_valid():
            weather_item = form.save(commit=False)
            weather_item.save()
            return redirect('/vxml/add/weather/')
    else:
        form = WeatherConditionForm()
    return render(request, 'fertilizer_website/weather_form.html', {'form':form})
