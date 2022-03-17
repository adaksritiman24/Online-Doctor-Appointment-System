from django.contrib.auth.forms import UserChangeForm
from mainapp.models import Patient
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class PatientEditForm(UserChangeForm):
    class Meta:
        model = Patient
        fields = ['first_name','last_name','gender','dob','contact']
        widgets = {
            'dob' : forms.DateInput(attrs={"type" : "date", "class" : 'form-control'}),
            'gender' : forms.Select(attrs={ 'class' : 'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'contact' : forms.TextInput(attrs={'class':'form-control'})
        }
        labels = {
            'dob':'Date of Birth'
        }