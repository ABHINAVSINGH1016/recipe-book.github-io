
# Create your views here.
from unicodedata import category
from django.shortcuts import render, redirect
from django.http import HttpResponse

from recipeapp.forms import product_form
from .models import Product
from django.core.paginator import Paginator
from django.template import loader
from .forms import product_form
# Create your views here.

def index(request):
    product_objects = Product.objects.all()

#search code

    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(recipe_type=item_name) or product_objects.filter(title=item_name) or product_objects.filter(category=item_name)
    
#paginator code
    paginator = Paginator(product_objects,4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

    return render(request,'index.html',{'product_objects': product_objects})

def detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    context={
        'product':product,
    }
    return render(request,'detail.html',context)

def create_item(request):
    form = product_form(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('recipeapp:index')

    return render(request,'item-form.html',{'form':form})   

def update_item(request,id):
    product = Product.objects.get(id=id)
    form = product_form(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('recipeapp:index')

    return render(request, 'item-form.html',{'form':form,'product':product})    

def delete_item(request,id):
    product_object = Product.objects.get(id=id)

    if request.method == 'POST':
        product_object.delete()
        return redirect('recipeapp:index')

    return render(request,'item-delete.html',{'product_object':product_object})    