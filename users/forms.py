from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import CustomerUser

User = get_user_model()

class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomerUser
        fields = ['username', 'email' , 'password1' , 'password2', 'gender', 'location', 'exercice', 'daily_goal']