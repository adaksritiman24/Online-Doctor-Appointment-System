from django.http import request
from django.shortcuts import redirect, render
from django.views import View
from accounts.models import Patient
from django.contrib.auth import logout
# Create your views here.

class PatientDashboard(View):
    def get(self, request):
        if request.user.is_authenticated:
            patient = Patient.objects.get(pk = request.user.id)
            context = {
                "patient" : patient,
            }
           
            return render(request, "patient/patient-dashboard.html", context=context)
        return redirect('/accounts/login/patient/')    
       

class IndexPage(View):
    def get(self, request):
        return render(request,"patient/index.html")        

class DoctorIndexPage(View):
    def get(self, request):
        return render(request,"doctor/index.html")

def logoutPatient(request):        
    logout(request)
    return redirect('/')
