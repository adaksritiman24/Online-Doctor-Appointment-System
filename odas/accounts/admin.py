from django.contrib import admin
from .models import Patient,Doctor
# Register your models here.

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','dob','gender','bio','email','charge','sun_start','sun_end')