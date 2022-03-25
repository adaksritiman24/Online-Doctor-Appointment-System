from django.contrib.auth.forms import UserChangeForm
from mainapp.models import Patient
from mainapp.models import Doctor
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

class DoctorEditForm(UserChangeForm):
    class Meta:
        model = Doctor
        fields = ['first_name','last_name','gender','dob','contact','speciality','bio','yoe',
        'charge','paypal','img','sun_start','sun_end','mon_start','mon_end','tue_start','tue_end','wed_start','wed_end',
        'thu_start','thu_end','fri_start','fri_end','sat_start','sat_end']

        widgets = {
            'dob' : DateInput(),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'contact': forms.TextInput(attrs={'class':'form-control'}),
            'bio': forms.Textarea(attrs={'class':'form-control','cols':20,'rows':4,'required':False}),
            'yoe': forms.TextInput(attrs={'class':'form-control'}),
            'charge': forms.TextInput(attrs={'class':'form-control'}),
            'paypal': forms.EmailInput(attrs={'class':'form-control'}),
            'speciality': forms.Select(attrs={'class':'form-control'}),
            'img' : forms.FileInput(attrs={'class':'form-control'}),

            'sun_start':forms.TimeInput(format='%H:%M',attrs={'type': 'time','required': False}),
            'sun_end':forms.TimeInput(format='%H:%M',attrs={'type': 'time','required': False}),
            'mon_start':forms.TimeInput(format='%H:%M',attrs={'type': 'time','required': False}),
            'mon_end':forms.TimeInput(format='%H:%M',attrs={'type': 'time','required': False}),
            'tue_start':forms.TimeInput(format='%H:%M',attrs={'type': 'time','required': False}),
            'tue_end':forms.TimeInput(format='%H:%M',attrs={'type': 'time','required': False}),
            'wed_start':forms.TimeInput(format='%H:%M',attrs={'type': 'time','required': False}),
            'wed_end':forms.TimeInput(format='%H:%M',attrs={'type': 'time','required': False}),
            'thu_start':forms.TimeInput(format='%H:%M',attrs={'type': 'time','required': False}),
            'thu_end':forms.TimeInput(format='%H:%M',attrs={'type': 'time','required': False}),
            'fri_start':forms.TimeInput(format='%H:%M',attrs={'type': 'time','required': False}),
            'fri_end':forms.TimeInput(format='%H:%M',attrs={'type': 'time','required': False}),
            'sat_start':forms.TimeInput(format='%H:%M',attrs={'type': 'time','required': False}),
            'sat_end':forms.TimeInput(format='%H:%M',attrs={'type': 'time','required': False}),
        }
    