from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic


from ..models.forms import CropForm
from ..models.models import Crop
from ..models.voicelabel import Language

#get all the audio data
def get_audio_data(crop, tutorial, language_code):
    languages = Language.objects.filter(code=language_code)
    tutorial_audio = []
    for language in languages:
        crop_audio = crop.voice_label.get_voice_fragment_url(language)              #audio for crop

        #Dict. for turorial audio
        for audio in tutorial:
            tutorial_audio.append({
                'voice_label':  audio,
                'name'       :  audio.name,
                'audio_url'  :  audio.get_voice_fragment_url(language)
            })


    audio_urls = {'crop': crop_audio,
             'tutorial': tutorial_audio
             }
    return audio_urls


#SHOW DETAIL PAGE CROPS
def detail_crop(request, id=id):
    #get all individual elements to show on the detail page
    crop = Crop.objects.get(id=id)
    fertilizers = crop.fertilizers.all()
    category = crop.category
    tutorial = crop.tutorial.voice_label.all()

    language_code = "en" #which language of the audio files

    #get all elements which has voices labels
    audio = get_audio_data(crop, fertilizers, tutorial, language_code)
    print(fertilizers)
    return render(request, 'mamoisson/detail_crop.html', {'crop': crop, 'fertilizers': fertilizers, 'category':category, 'audio': audio})

#ADD NEW CROP
def add_crop(request):
    if request.method == "POST":
        form = CropForm(request.POST)
        if form.is_valid():
            crop_item = form.save(commit=False)
            crop_item.save()
            return redirect('/vxml/mamoisson/crop/' + str(crop_item.id) + '/')
    else:
        form = CropForm()
    return render(request, 'mamoisson/add/crop.html', {'crop':form})


#EDIT CROP
def edit_crop(request, id=None):
    item = get_object_or_404(Crop, id=id)
    form = CropForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('/vxml/mamoisson/crop/' + str(item.id) + '/')
    return render(request, 'mamoisson/edit/crop.html', {'crop':form})

#DELETE CROP
def delete_crop(request, id=id):
    crop = Crop.objects.get(pk=id) #get the crop which needed be deleted
    crop.delete()
    return redirect('/vxml/mamoisson/')