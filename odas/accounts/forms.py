from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Patient


class DateInput(forms.DateInput):
    input_type = 'date'

class PatientRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label = 'Password',widget = forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label = 'Retype Password',widget = forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = Patient
        fields = ['first_name','last_name','gender','dob','contact','username','email']
        widgets = {
            'dob' : DateInput(),
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'contact': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            
        }
        labels = {
            'dob':'Date of Birth'
        }




