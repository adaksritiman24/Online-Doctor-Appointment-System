from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Patient(User):
    CHOICES = [
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others'),
    ]
    gender = models.CharField(null=False, max_length=8, choices=CHOICES)
    contact = models.CharField(max_length=12)
    dob = models.DateField()

