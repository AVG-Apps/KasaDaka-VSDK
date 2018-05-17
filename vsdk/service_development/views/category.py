from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic


from ..models.forms import CategoryForm
from ..models.models import Category
from ..models.voicelabel import Language

#SHOW OVERVIEW CATEGORIES
def overview_category(request, id=id):
    latest_category_list = Category.objects.all()
    context = {'latest_category_list': latest_category_list}
    return render(request, 'mamoisson/overview/category.html', context)


#ADD CATEGORY
def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category_item = form.save(commit=False)
            category_item.save()
            return redirect('/vxml/mamoisson/category')
    else:
        form = CategoryForm()
    return render(request, 'mamoisson/add/category.html', {'category':form})

#EDIT CATEGORY
def edit_category(request, id=None):
    item = get_object_or_404(Category, id=id)
    form = CategoryForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('/vxml/mamoisson/category/')
    return render(request, 'mamoisson/edit/category.html', {'category':form})


#DELETE CATEGORY
def delete_category(request, id=id):
    category = Category.objects.get(pk=id) #get the fertilizer which needed be deleted
    category.delete()
    return redirect('/vxml/mamoisson/category/')