from django.db import models
from .voicelabel import VoiceLabel

#Crop model with all attributes
class Crop(models.Model):
    crop_name = models.CharField(max_length=30)
    crop_img_url = models.URLField(max_length=200)

    def __str__(self):
        return self.crop_name

#Weather model with all attributes
class Weather(models.Model):
    weather_condition = models.CharField(max_length=30)

    def __str__(self):
        return self.weather_condition

#Fertilizer model with all attributes
class Fertilizer(models.Model):
    fertilizer_name = models.CharField(max_length=30, default='', blank=True)
    description = models.TextField(default='', blank=True)
    subdescription = models.CharField(max_length=20)

    weather_condition_list = models.ForeignKey('Weather', on_delete=models.CASCADE)
    crop_list = models.ForeignKey('Crop', on_delete=models.CASCADE)

    def __str__(self):
        return self.fertilizer_name