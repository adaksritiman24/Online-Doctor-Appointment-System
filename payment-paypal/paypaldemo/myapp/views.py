from django.http.response import HttpResponse
from .models import Patient, Doctor
from django.shortcuts import redirect, render

# Create your views here.

def home(request):
    patient =Patient.objects.get(pk = 2)
    doctor = Doctor.objects.get(pk = 2)
    print(patient.paystatus)
    return render(request, "myapp/home.html", {'patient':patient, 'doctor':doctor})

def success(request):
    print(request.GET['status'], request.GET['userid'])
    if request.GET['status'] == 'success':
        Patient.objects.filter(id = request.GET['userid']).update(paystatus = 1)    
    else:
        print("payment Failed")    
    return HttpResponse("Request is awesome") 