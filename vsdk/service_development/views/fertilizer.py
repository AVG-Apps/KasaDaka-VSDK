# from django.template import loader
# from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
# from django.http import HttpResponseRedirect, HttpResponse
# from django.urls import reverse

from ..models.forms import FertilizerForm, CropForm, WeatherConditionForm, TutorialsFrom
from ..models.models import Fertilizer, Crop, Weather, Tutorials
from ..models.voicelabel import Language, VoiceLabel

# from . import base

#Shows the Main page
def main_page(request):
    latest_fertilizer_list = Fertilizer.objects.all()
    context = {'latest_fertilizer_list': latest_fertilizer_list}
    return render(request, 'fertilizer_website/main_page.html', context)


#Shows the Fertilizer detail page
def fertilizer(request, id=id):
    fertilizer = Fertilizer.objects.get(id=id)
    crops = fertilizer.crops.all()
    # weather = fertilizer.weather.all()
    # tutorials = fertilizer.tutorials.all()

    languages = Language.objects.filter(code="en")
    for language in languages:
        fertilizer_audio = fertilizer.voice_label.get_voice_fragment_url(language)

        # fertilizer_audio = fertilizer.voice_label.get_voice_fragment_url(language)
        # crops_audio = crops.voice_label.get_voice_fragment_url(language)
        # weather_audio = weather.voice_label.get_voice_fragment_url(language)
        # tutorials_audio = tutorials.voice_label.get_voice_fragment_url(language)

    # 'crop': crops_audio, 'weather': weather_audio, 'tutorials': tutorials_audio
    audio = {'fertilizer': fertilizer_audio, }


    return render(request, 'fertilizer_website/detail.html', {'fertilizer': fertilizer, 'crops': crops, 'audio': audio})


#Shows the voice XML application
def voice_app(request):
    latest_fertilizer_list = Fertilizer.objects.all()
    context = {'latest_fertilizer_list': latest_fertilizer_list}
    return render(request, 'main-en-1.xml', context,  content_type='text/xml')

#add new fertilizer to the the index page
def add_fertilizer(request):
    print('hallo')
    print(request.method)
    if request.method == "POST":
        print('is posted')
        form = FertilizerForm(request.POST)
        if form.is_valid():
            print('is valid')
            fertilizer_item = form.save(commit=False)
            fertilizer_item.save()
            return redirect('/vxml/fertilizer/' + str(fertilizer_item.id) + '/')
    else:
        form = FertilizerForm()
    return render(request, 'fertilizer_website/fertilizer_form.html', {'fertilizer':form})

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
    return render(request, 'fertilizer_website/crop_form.html', {'crop':form})


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
    return render(request, 'fertilizer_website/weather_form.html', {'weather':form})


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
    return render(request, 'fertilizer_website/tutorial_form.html', {'tutorial':form})


#edit the fertilizer on the detail page
def edit_fertilizer(request, id=None):
    item = get_object_or_404(Fertilizer, id=id)
    form = FertilizerForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('/vxml/fertilizer/' + str(item.id) + '/')
    return render(request, 'fertilizer_website/fertilizer_form.html', {'fertilizer':form})
