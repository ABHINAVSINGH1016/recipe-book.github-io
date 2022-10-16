from unicodedata import category
from django.db import models
# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=200,default='title')
    items = models.TextField(default='ingredient')
    item_ingredients = models.TextField(default='ingredient')
    recipe =models.TextField(default='recipe')
    recipe_aditonal = models.TextField(default='recipe')
    image = models.CharField(max_length = 400,default='image')
    recipe_type = models.CharField(max_length=200,default='food type')
    category = models.CharField(max_length=200,default= 'food type')        