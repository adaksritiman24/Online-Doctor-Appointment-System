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

class Doctor(User):
    CHOICES = [
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others'),
    ]
    SPECIALITIES= [
        ('Podiatrist','Podiatrist'),
        ('General','General'),
        ('Pediatrician','Pediatrician'),
        ('Endocrinologist','Endocrinologist'),
        ('NeuroLogist','Neurologist'),
        ('Rheumatologist','Rheumatologist'),
        ('Alergist','Allergist'),
        ('Psychiatrist','Psychiatrist'),
    ]
    gender = models.CharField(null = False, max_length=8, choices=CHOICES)
    contact = models.CharField(max_length=12)
    dob = models.DateField()
    speciality = models.CharField(null=False, choices = SPECIALITIES, max_length=20)
    bio = models.TextField(null=True, max_length=800)
    yoe = models.IntegerField()
    charge = models.DecimalField(decimal_places=2,max_digits=7, max_length = 10)
    
    sun_start = models.TimeField(null=True)
    sun_end = models.TimeField(null = True)
    
    mon_start = models.TimeField(null = True)
    mon_end = models.TimeField(null = True)
    
    tue_start = models.TimeField(null = True)
    tue_end = models.TimeField(null = True)
    
    wed_start = models.TimeField(null = True)
    wed_end = models.TimeField(null = True)
    
    thu_start = models.TimeField(null = True)
    thu_end = models.TimeField(null = True)
    
    fri_start = models.TimeField(null = True)
    fri_end = models.TimeField(null = True)
    
    sat_start = models.TimeField(null = True)
    sat_end = models.TimeField(null = True)