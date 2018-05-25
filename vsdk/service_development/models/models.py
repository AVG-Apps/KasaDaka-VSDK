from django.db import models
from .voicelabel import VoiceLabel


class Category(models.Model):
    name = models.CharField(max_length=30, default='', blank=True)

    def __str__(self):
        return self.name

class Tutorials(models.Model):
    name = models.CharField(max_length=30, default='', blank=True)
    voice_label = models.ManyToManyField(VoiceLabel, blank=True)

    def __str__(self):
        return self.name

class Fertilizer(models.Model):
    name = models.CharField(max_length=30, default='', blank=True)
    image_url = models.URLField(null=True)

    def __str__(self):
        return self.name

class Crop(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(default='', blank=True)
    img_url = models.URLField()

    fertilizers = models.ManyToManyField(Fertilizer)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    tutorial = models.ForeignKey(Tutorials, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
