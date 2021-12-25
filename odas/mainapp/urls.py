from django.urls import path
from . import views
urlpatterns = [
    #ppatient stuffs
    path('dashboard/patient/',views.PatientDashboard.as_view(), name="pd"),
    path('',views.IndexPage.as_view(), name="index"),
    path('logout/patient/',views.logoutPatient, name="logout_p"),

    #doctor stuffs
    path('doc',views.DoctorIndexPage.as_view(), name="index_d"),
    path('logout/doctor/',views.logoutDoctor, name="logout_d"),
    path('dashboard/doctor/',views.DoctorDashboard.as_view(), name="dd"),

    #patient appointment
    path('makeappointment/<int:doctorid>/',views.makeAppointment, name="makeApp"),
    path('appointments/patient/',views.PatientAppointmentPage, name="p_app"),

    #patient appointment date and times
    path('searchdate', views.getTimesForParticularDay, name = "gtfpd"),

    #doctor-appointment
    path('appointments/doctor/',views.DoctorAppointmentPage, name="d_app"),
]
