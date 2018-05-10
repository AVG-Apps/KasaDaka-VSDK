from django.db import models
from .voicelabel import VoiceLabel

#Crop model with all attributes
class Crop(models.Model):
    name = models.CharField(max_length=30)
    img_url = models.URLField()
    audio_url = models.URLField( null=True)

    def __str__(self):
        return self.name

#Weather model with all attributes
class Weather(models.Model):
    name = models.CharField(max_length=30)
    image_url = models.URLField(null=True)
    audio_url = models.URLField(null=True)

    def __str__(self):
        return self.name


class Tutorials(models.Model):
    name = models.CharField(max_length=30, default='', blank=True)
    description = models.TextField(default='', blank=True)
    voice_label = models.ManyToManyField(VoiceLabel, blank=True)


    def __str__(self):
        return self.name

#Fertilizer model with all attributes
class Fertilizer(models.Model):
    name = models.CharField(max_length=30, default='', blank=True)
    description = models.TextField(default='', blank=True)
    image_url = models.URLField(null=True)

    crops = models.ManyToManyField(Crop, blank=True)
    weather_condition = models.ForeignKey('Weather', on_delete=models.CASCADE, null=True)

    voice_label = models.ForeignKey(VoiceLabel, on_delete=models.CASCADE, null=True)
    tutorial = models.ForeignKey(Tutorials, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


