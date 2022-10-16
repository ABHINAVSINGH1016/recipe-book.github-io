from socket import fromshare
from django import forms
from .models import Product

class product_form(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title','items','item_ingredients','recipe','recipe_aditonal','image','recipe_type','category']