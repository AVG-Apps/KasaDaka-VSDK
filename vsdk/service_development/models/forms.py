from django.forms import ModelForm
from .models import Fertilizer, Crop, Weather

class FertilizerForm(ModelForm):
    class Meta:
        model = Fertilizer
        fields = '__all__'

class CropForm(ModelForm):
    class Meta:
        model = Crop
        fields = '__all__'


class WeatherConditionForm(ModelForm):
    class Meta:
        model = Weather
        fields = '__all__'
