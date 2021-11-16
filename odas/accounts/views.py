from django.shortcuts import redirect, render
from django.views import View
from .forms import PatientRegistrationForm
from .models import Patient
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

# Create your views here.

def isPatient(user):
    try:
        Patient.objects.get(pk = user.id)
        return True
    except Exception as exe:
        return False

class PatientRegistration(View):
    
    def get(self, request):
        if not request.user.is_authenticated:
            form = PatientRegistrationForm()
            context = {
                'fm':form,
            }
            return render(request,"patient-registration.html",context=context)
        return redirect('/dashboard/patient/')

    def post(self, request):
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            users = User.objects.filter(email = form.cleaned_data["email"])
            if users:
                print("Email already exists!")
                messages.error(request,'Email already exists!')
            else:
                form.save()
                currentUser = User.objects.get(username = form.cleaned_data["username"])
                login(request, currentUser)
                messages.success(request,'New Registration successfull')
                return redirect("/dashboard/patient/")   
        
        context = {
            'fm':form,
        }
        return render(request,"patient-registration.html",context=context)

class PatientLogin(View):
    
    def get(self, request):
        if not request.user.is_authenticated:
            context = {
                
            }
            return render(request,'patient-login.html',context=context)
        return redirect('/dashboard/patient/')


    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        print(username)
        user = authenticate(username = username, password=password)
        if user:
            if isPatient(user):
                login(request,user)
                messages.success(request,'Hello User')
                return redirect('/dashboard/patient/')

        messages.error(request, "Invalid Credentials!")
        return redirect('/accounts/login/patient/')


