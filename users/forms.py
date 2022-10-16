from operator import length_hint
from sys import maxsize
from unittest.util import _MAX_LENGTH
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from phone_field import PhoneField

class Registerform(UserCreationForm):
    email = forms.EmailField()
    contact = forms.IntegerField()


    class Meta:
        model = User
        fields = ['username','email','contact','password1','password2']