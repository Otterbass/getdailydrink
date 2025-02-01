from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomerUser(AbstractUser):
    GENDER_CHOICES = [
        ('F', 'Female'),
        ('M', 'Male')
    ]
    EXERCICE_CHOICES = [
        ('cardio' , 'Cardio'),
        ('weights', 'Weights'),
        ('none', 'None')
    ]
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    location = models.CharField(max_length=250)
    exercises_type = models.CharField(max_length=50, choices=EXERCICE_CHOICES)
    daily_goal = models.FloatField(default=2.5)

    def __str__(self):
        return self.username