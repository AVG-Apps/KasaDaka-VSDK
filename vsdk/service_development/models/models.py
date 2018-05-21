from django.db import models
from .voicelabel import VoiceLabel


class Category(models.Model):
    name = models.CharField(max_length=30, default='', blank=True)

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
    image_url = models.URLField(null=True)
    description = models.TextField(default='', blank=True)
    voice_label = models.ForeignKey(VoiceLabel, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


#Crop model with all attributes
class Crop(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(default='', blank=True)
    img_url = models.URLField()
    voice_label = models.ForeignKey(VoiceLabel, on_delete=models.CASCADE)

    fertilizers = models.ManyToManyField(Fertilizer)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    voice_label = models.ForeignKey(VoiceLabel, on_delete=models.CASCADE)
    tutorial = models.ForeignKey(Tutorials, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
