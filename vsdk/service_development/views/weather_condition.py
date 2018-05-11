from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic


from ..models.forms import FertilizerForm, CropForm, WeatherConditionForm, TutorialsFrom
from ..models.models import Fertilizer, Crop, Weather, Tutorials
from ..models.voicelabel import Language, VoiceLabel


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
    return render(request, 'mamoisson/insert/weather.html', {'weather':form})