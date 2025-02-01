from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User= get_user_model()

class UserWaterIntake(models.Model):
    # GENDER_CHOICE = [
    #     ('M', 'Male'),
    #     ('F', 'Female')
    # ]
    EXERCICE_CHOICES = [
        ('cardio' , 'Cardio'),
        ('weights', 'Weights'),
        ('none', 'None')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # gender = models.CharField(max_length=20, choices=GENDER_CHOICE)
    # location = models.CharField(max_length=100)
    exercises_type = models.CharField(max_length=50, choices=EXERCICE_CHOICES)
    water_amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)