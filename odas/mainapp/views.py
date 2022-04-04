from django.db.models.aggregates import Count
from django.http import request, JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from accounts.models import Patient, Doctor
from accounts.views import isDoctor, isPatient
from edit.models import Report 
from django.contrib.auth import logout
from .models import Appointment
from datetime import date, datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q 
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
# Create your views here.

class PatientDashboard(View):
    def get(self, request):
        if request.user.is_authenticated:
            if isDoctor(request.user):
                return redirect('/dashboard/doctor/')
            patient = Patient.objects.get(pk = request.user.id)
            doctors = Doctor.objects.all()

            context = {
                "patient" : patient,
                "doctors": doctors,
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


#appointment------------------

def makeAppointment(request, doctorid, date, time):
    date = datetime.strptime(date,'%d-%m-%Y').date()
    time = datetime.strptime(time, '%H:%M').time()
    doctor = Doctor.objects.get(pk = doctorid)
    patient = Patient.objects.get(pk = request.user.id)

    app_start_time = datetime.combine(date=date, time=time)
    app_end_time = timezone.make_aware(app_start_time+timedelta(minutes=30))

    appointment = Appointment(patient = patient, doctor = doctor, date=date, time=time, date_time_start = app_start_time, date_time_end = app_end_time, status="upcomming") 
    appointment.save()

    return redirect('/appointments/patient/')


def PatientAppointmentPage(request):
    currentTime =  timezone.make_aware(datetime.now())
    appointments = Appointment.objects.filter(patient = request.user)
    app_over = appointments.filter(Q(date_time_end__lt = currentTime))
    app_active = appointments.filter(Q(date_time_end__gte = currentTime) & Q(date_time_start__lte = currentTime))
    app_upcomming = appointments.filter(Q(date_time_start__gt = currentTime))

    context = {
        'app_over':app_over,
        'app_active': app_active,
        'app_upcomming': app_upcomming,
    }
    return render(request,"patient/patient-appointment.html",context= context)

class DoctorAppointmentPage(View):

    def get(self,request):
        currentTime = timezone.make_aware(datetime.now())
        appointments = Appointment.objects.filter(doctor = request.user)
        app_over = appointments.filter(Q(date_time_end__lt = currentTime))
        app_active = appointments.filter(Q(date_time_end__gte = currentTime) & Q(date_time_start__lte = currentTime))
        app_upcomming = appointments.filter(Q(date_time_start__gt = currentTime))
        context = {
            'appointments': appointments,
            'app_over' : app_over,
            'app_active' : app_active,
            'app_upcomming' : app_upcomming
        }
        return render(request,"doctor/doctor-appointment.html",context= context)

    def post(self, request):
        try:
            appointmentNumber = int(request.POST['appNo'])
            prescriptionFile = request.FILES[f'p-file-{appointmentNumber}']
            fs = FileSystemStorage('media/prescriptions/')
            file = fs.save(prescriptionFile.name, prescriptionFile)

            Appointment.objects.filter(id=appointmentNumber).update(prescription = 'prescriptions/'+file)

        except Exception as e: 
            print(e)  
            pass 
        return redirect('/appointments/doctor/')    



#date and time selection---------------------------------------

def getStartEndTime(doctor, day, q_date):
    time_start = None
    time_end = None 
    if day == 1:
        time_start = doctor.mon_start
        time_end = doctor.mon_end
    elif day == 2:
        time_start = doctor.tue_start
        time_end = doctor.tue_end
    elif day == 3:
        time_start = doctor.wed_start
        time_end = doctor.wed_end
    elif day == 4:
        time_start = doctor.thu_start
        time_end = doctor.thu_end
    elif day == 5:
        time_start = doctor.fri_start
        time_end = doctor.fri_end
    elif day == 6:
        time_start = doctor.sat_start
        time_end = doctor.sat_end
    elif day == 7:
        time_start = doctor.sun_start
        time_end = doctor.sun_end
    try:    
        return datetime.combine(q_date, time_start), datetime.combine(q_date, time_end)    
    except Exception as exe:
        return None, None

def getAvailableTimes(booked_slots, duration, start_time, end_time):
    current = start_time
    count = 0
    available = {}
    while True:
        if current not in booked_slots:
            count +=1
            available[count] = current
        current +=duration
        if current + duration > end_time:
            break
    return available

@csrf_exempt
def getTimesForParticularDay(request):
    type = request.POST['type']
    date = request.POST['date']
    doctor_id = request.POST['doctor_id']
    print(type, date, doctor_id)
    
    duration = timedelta(minutes=30)

    if type == "dateSearch":

        q_date = datetime.strptime(date,"%Y-%m-%d").date()
        day = q_date.isoweekday()
        #get all appointment times for the date
        appointments = Appointment.objects.filter(Q(doctor_id=doctor_id) & Q(date=q_date) & (Q(status="upcomming") | Q(status="ongoing")))
        print(appointments)
        
        #get Doctor start and end times
        doctor = Doctor.objects.get(pk =doctor_id)
        start_time, end_time = getStartEndTime(doctor, day, q_date)
        print(start_time, end_time)

        booked_slots = set()
        
        for appointment in appointments:
            booked_slots.add(
                datetime.combine(q_date, appointment.time)
            )
        available_slots = {}
        if start_time:
            available_slots = getAvailableTimes(booked_slots, duration, start_time, end_time)
        response = {
            'success' : 'success '+ doctor_id,
            'day' : q_date.isoweekday(),
            'gone' : datetime.today().date() > q_date,
            'available': available_slots
        }
    return JsonResponse(response)

# view prescription------------------------------------------
def viewPrescription(request, app_no):
    appointment = Appointment.objects.get(pk = app_no)
    context = {
        "appointment" : appointment,
    }
    return render( request, 'prescription/viewer.html', context=context)


#fetch patient reports

def patientReports(request, p_id):
    try:
        reports = list(Report.objects.filter(patient_id = int(p_id)).values())
    except Exception:
        reports = []    
        
    return JsonResponse(reports, safe=False)