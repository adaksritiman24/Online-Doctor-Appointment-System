from django.db import models

# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=70)
    paystatus = models.IntegerField()
class Doctor(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
