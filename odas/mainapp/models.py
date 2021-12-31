from django.db import models
from django.db.models.base import Model

from accounts.models import Patient, Doctor

# Create your models here.
class Appointment(models.Model):
    STATUS = [
        ("finished","finished"),
        ("upcomming","upcomming"),
        ("ongoing","ongoing"),
    ]
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    date_time_start = models.DateTimeField(null=True, blank=True)
    date_time_end = models.DateTimeField(null=True, blank=True)
    status = models.CharField(null = True, blank = True, max_length=20, choices=STATUS)
    prescription = models.FileField(upload_to='prescriptions/%Y/%m/%d', null=True, blank=True)


    