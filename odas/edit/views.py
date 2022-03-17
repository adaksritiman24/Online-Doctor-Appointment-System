from cmath import log
from contextlib import redirect_stderr
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import PatientEditForm
from accounts.models import Patient
# Create your views here.

class PatientEditPage(View):
    def get(self, request):
        patient = Patient.objects.get(pk = request.user.id)
        fm = PatientEditForm(instance = patient)
        return render(request, "patient/patient-edit.html",{'form' : fm})

    def post(self, request):
        patient = Patient.objects.get(pk = request.user.id)
        fm = PatientEditForm(instance = patient, data = request.POST)
        if fm.is_valid():
            fm.save()
            print("updated")
            return redirect('/edit/patient/')
        return HttpResponse("Unable to Proceed!");    
