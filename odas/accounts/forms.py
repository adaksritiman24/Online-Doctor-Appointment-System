from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Patient, Doctor


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

class DoctorRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label = 'Password',widget = forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label = 'Retype Password',widget = forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = Doctor
        fields = ['first_name','last_name','gender','dob','contact','username','email','speciality','bio','yoe',
        'charge','sun_start','sun_end','mon_start','mon_end','tue_start','tue_end','wed_start','wed_end',
        'thu_start','thu_end','fri_start','fri_end','sat_start','sat_end']

        sun_start = forms.TimeField()
        widgets = {
            'dob' : DateInput(),
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'contact': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'bio': forms.Textarea(attrs={'class':'form-control','cols':20,'rows':4}),
            'yoe': forms.TextInput(attrs={'class':'form-control'}),
            'charge': forms.TextInput(attrs={'class':'form-control'}),
            
            'sun_start':forms.TimeInput(format='%H:%M',attrs={'type': 'time'}),
            'sun_end':forms.TimeInput(format='%H:%M',attrs={'type': 'time'}),
            'mon_start':forms.TimeInput(format='%H:%M',attrs={'type': 'time'}),
            'mon_end':forms.TimeInput(format='%H:%M',attrs={'type': 'time'}),
            'tue_start':forms.TimeInput(format='%H:%M',attrs={'type': 'time'}),
            'tue_end':forms.TimeInput(format='%H:%M',attrs={'type': 'time'}),
            'wed_start':forms.TimeInput(format='%H:%M',attrs={'type': 'time'}),
            'wed_end':forms.TimeInput(format='%H:%M',attrs={'type': 'time'}),
            'thu_start':forms.TimeInput(format='%H:%M',attrs={'type': 'time'}),
            'thu_end':forms.TimeInput(format='%H:%M',attrs={'type': 'time'}),
            'fri_start':forms.TimeInput(format='%H:%M',attrs={'type': 'time'}),
            'fri_end':forms.TimeInput(format='%H:%M',attrs={'type': 'time'}),
            'sat_start':forms.TimeInput(format='%H:%M',attrs={'type': 'time'}),
            'sat_end':forms.TimeInput(format='%H:%M',attrs={'type': 'time'}),
        }
        labels = {
            'dob':'Date of Birth'
        }



