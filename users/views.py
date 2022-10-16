from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import Registerform
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = Registerform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'welcome {username}, your account is created')
            return redirect('login')
    else:
        form = Registerform()
    return render(request,'register.html',{'form':form})

@login_required
def profilepage(request):
    return render(request, 'profile.html')