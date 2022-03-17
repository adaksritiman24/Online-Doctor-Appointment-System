from django.db import models
from accounts.models import Patient
# Create your models here.

class Report(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    report = models.FileField(upload_to= 'patient_reports/%y')
    name = models.CharField(max_length=40)
