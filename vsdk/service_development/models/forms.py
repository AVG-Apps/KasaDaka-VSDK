from django.forms import ModelForm

from .models import Crop, Category, Fertilizer, Tutorials

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class CropForm(ModelForm):
    class Meta:
        model = Crop
        fields = '__all__'


class FertilizerForm(ModelForm):
    class Meta:
        model = Fertilizer
        fields = '__all__'


class TutorialsFrom(ModelForm):
    class Meta:
        model = Tutorials
        fields = '__all__'




