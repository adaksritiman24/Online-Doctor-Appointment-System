from django.http import request
from django.shortcuts import redirect, render
from django.views import View
from accounts.models import Patient, Doctor
from accounts.views import isDoctor, isPatient
from django.contrib.auth import logout
# Create your views here.

class PatientDashboard(View):
    def get(self, request):
        if request.user.is_authenticated:
            if isDoctor(request.user):
                return redirect('/dashboard/doctor/')
            patient = Patient.objects.get(pk = request.user.id)
            context = {
                "patient" : patient,
            }
           
            return render(request, "patient/patient-dashboard.html", context=context)
        return redirect('/accounts/login/patient/')    
       
class DoctorDashboard(View):
    def get(self, request):
        if request.user.is_authenticated:

            if isPatient(request.user):
                return redirect('/dashboard/patient/')

            doctor = Doctor.objects.get(pk = request.user.id)
            context = {
                "doctor" : doctor,
            }
           
            return render(request, "doctor/doctor-dashboard.html", context=context)
        return redirect('/accounts/login/doctor/')    
       

class IndexPage(View):
    def get(self, request):
        return render(request,"patient/index.html")        

class DoctorIndexPage(View):
    def get(self, request):
        return render(request,"doctor/index.html")

def logoutPatient(request):        
    logout(request)
    return redirect('/')

def logoutDoctor(request):        
    logout(request)
    return redirect('/doc')
