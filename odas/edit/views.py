from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from .models import Report
from .forms import PatientEditForm
from .forms import DoctorEditForm
from accounts.models import Patient
from accounts.models import Doctor

# Create your views here.

class PatientEditPage(View):
    def get(self, request):
        patient = Patient.objects.get(pk = request.user.id)
        patient_reports = Report.objects.filter(patient = patient)
        fm = PatientEditForm(instance = patient)
        return render(request, "patient/patient-edit.html",{'form' : fm, 'reports':patient_reports})

    def post(self, request):
        patient = Patient.objects.get(pk = request.user.id)
        if request.POST['type']=="user":
            fm = PatientEditForm(instance = patient, data = request.POST)
            if fm.is_valid():
                fm.save()
                print("updated")
                messages.success(request, "Details Updated Sussessfully!")
                return redirect('/edit/patient/')
            messages.error(request, "Coudn't update details!")    
            return redirect('/edit/patient/')
        else:
            try:
                report = request.FILES['report']    
                description = request.POST['description']
                
                report = Report(patient=patient, report= report, name = description)
                report.save();
                messages.success(request, "Report Uploaded Sussessfully!")
                return redirect('/edit/patient/')
            except Exception:
                messages.error(request, "Coudn't Upload Report!")
                return redirect('/edit/patient/')    


def viewReport(request, rep_no):
    report = Report.objects.get(pk = rep_no)
    context = {
        "report" : report,
    }
    return render( request, 'reports/viewer.html', context=context)

class DoctorEditPage(View):
    def get(self, request):
        doctor = Doctor.objects.get(pk=request.user.id)
        fm = DoctorEditForm(instance = doctor)
        return render(request, "doctor/doctor-edit.html", {"form" : fm})
