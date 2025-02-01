from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomerUser(AbstractUser):
    GENDER_CHOICES = [
        ('F', 'Female'),
        ('M', 'Male')
    ]
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    location = models.CharField(max_length=250)
    exercice = models.CharField(max_length=250)
    daily_goal = models.FloatField(default=2.0)

    def __str__(self):
        return self.username