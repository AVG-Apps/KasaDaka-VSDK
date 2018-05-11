# from django.template import loader
# from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
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

#Shows the Main page
def team_page(request):
    return render(request, 'fertilizer_website/team_page.html')



def get_audio_url(fertilizer, crops, weather_condition, tutorial, language_code):
    languages = Language.objects.filter(code=language_code)
    crops_audio = []
    tutorial_audio = []
    for language in languages:
        fertilizer_audio = fertilizer.voice_label.get_voice_fragment_url(language)
        weather_condition_audio = weather_condition.voice_label.get_voice_fragment_url(language)

        for audio in tutorial:
            tutorial_audio.append({
                'voice_label':  audio,
                'name'       :  audio.name,
                'audio_url'  :  audio.get_voice_fragment_url(language)
            })


        for audio in crops:
            crops_audio.append({
                'voice_label':  audio.voice_label,
                'name'       :  audio.voice_label.name,
                'audio_url'  :  audio.voice_label.get_voice_fragment_url(language)
            })

    audio_urls = {'fertilizer': fertilizer_audio,
             'crops': crops_audio,
             'weather': weather_condition_audio,
             'tutorial': tutorial_audio
             }
    return audio_urls


#Shows the Fertilizer detail page
def fertilizer(request, id=id):
    fertilizer = Fertilizer.objects.get(id=id)
    crops = fertilizer.crops.all()
    weather_condition = fertilizer.weather_condition
    tutorial = fertilizer.tutorial.voice_label.all()
    language_code = "en"

    audio = get_audio_url(fertilizer, crops, weather_condition, tutorial, language_code)

    return render(request, 'fertilizer_website/detail.html', {'fertilizer': fertilizer, 'crops': crops, 'audio': audio})


#Shows the voice XML application
def voice_app(request):
    latest_fertilizer_list = Fertilizer.objects.all()
    context = {'latest_fertilizer_list': latest_fertilizer_list}
    return render(request, 'main-en-1.xml', context,  content_type='text/xml')

#add new fertilizer to the the index page
def add_fertilizer(request):
    print(request.method)
    if request.method == "POST":
        form = FertilizerForm(request.POST)
        if form.is_valid():
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


#delete the fertilizer on the detail page
def delete_fertilizer(request, id=id):
    fertilizer = Fertilizer.objects.get(pk=id)
    print(fertilizer)
    fertilizer.delete()
    print(fertilizer)
    return redirect('/vxml/fertilizer/')
