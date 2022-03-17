from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import Report
from .forms import PatientEditForm
from accounts.models import Patient
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
                return redirect('/edit/patient/')
            return HttpResponse("Unable to Proceed!"); 
        else:
            try:
                report = request.FILES['report']    
                description = request.POST['description']
                
                report = Report(patient=patient, report= report, name = description)
                report.save();
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