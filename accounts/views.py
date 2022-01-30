from django.contrib.auth import forms
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserRegisterForm


# Create your views here.


def signup(request):
    if request.method =='POST':
     form =UserRegisterForm(request.POST)
     if form.is_valid():
         form.save()
         username =form.cleaned_data.get('username')
         messages.success(request, f'Your account has been created! you are able to login {username}!')
         return redirect('login')
    else:
        form =UserRegisterForm()     
    return render(request, 'accounts/signup.html',{'form':form})

       


def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    return render(request, 'accounts/logout.html')

