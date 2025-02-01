from django import forms
from .models import UserWaterIntake
from users.models import CustomerUser


class WaterIntakeForm(forms.ModelForm):
    class Meta:
        model = UserWaterIntake
        fields = ['exercises_type', 'water_amount']