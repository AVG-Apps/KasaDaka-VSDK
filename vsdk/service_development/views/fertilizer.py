from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic

from ..models.forms import FertilizerForm
from ..models.models import Fertilizer
from ..models.voicelabel import Language

#get all the data which
def get_audio_data(fertilizer, crops, weather_condition, tutorial, language_code):
    languages = Language.objects.filter(code=language_code)
    crops_audio = []
    tutorial_audio = []
    for language in languages:
        fertilizer_audio = fertilizer.voice_label.get_voice_fragment_url(language)               #audio for fertilizer
        weather_condition_audio = weather_condition.voice_label.get_voice_fragment_url(language) #audio for weather condition

        #Dict. for turorial audio
        for audio in tutorial:
            tutorial_audio.append({
                'voice_label':  audio,
                'name'       :  audio.name,
                'audio_url'  :  audio.get_voice_fragment_url(language)
            })

        #Dict. for crop audio
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


#DETAIL PAGE
def fertilizer(request, id=id):
    #get all individual elements to show on the detail page
    fertilizer = Fertilizer.objects.get(id=id)
    crops = fertilizer.crops.all()
    weather_condition = fertilizer.weather_condition
    tutorial = fertilizer.tutorial.voice_label.all()

    language_code = "en" #which language of the audio files

    #get all elements which has voices labels
    audio = get_audio_data(fertilizer, crops, weather_condition, tutorial, language_code)

    return render(request, 'mamoisson/detail.html', {'fertilizer': fertilizer, 'crops': crops, 'audio': audio})

#ADD FERTILIZER
def add_fertilizer(request):
    if request.method == "POST":
        form = FertilizerForm(request.POST)
        if form.is_valid():
            fertilizer_item = form.save(commit=False)
            fertilizer_item.save()
            return redirect('/vxml/fertilizer/' + str(fertilizer_item.id) + '/')
    else:
        form = FertilizerForm()
    return render(request, 'mamoisson/insert/fertilizer.html', {'fertilizer':form})

#EDIT FERTILIZER
def edit_fertilizer(request, id=None):
    item = get_object_or_404(Fertilizer, id=id)
    form = FertilizerForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('/vxml/fertilizer/' + str(item.id) + '/')
    return render(request, 'mamoisson/insert/fertilizer.html', {'fertilizer':form})

#DELETE FERTILIZER
def delete_fertilizer(request, id=id):
    fertilizer = Fertilizer.objects.get(pk=id) #get the fertilizer which needed be deleted
    fertilizer.delete()
    return redirect('/vxml/fertilizer/')