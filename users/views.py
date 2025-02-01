from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import CustomerUser
from .forms import RegistrationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout

# Create your views here.

# REGISTER VIEW LOGIC

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form' : form})

# LOGIN VIEW LOGIC

def user_login(request):
    if request.method == 'POST':
        username = request.POST ['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'registration/login.html')

def logout_view(request):
    logout()
    return redirect('home')


# FOR TEST ONLY
def home(request):
    return HttpResponse('home')