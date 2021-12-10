from django.urls import path
from . import views
urlpatterns = [
    path('dashboard/patient/',views.PatientDashboard.as_view(), name="pd"),
    path('',views.IndexPage.as_view(), name="index"),
    path('logout/patient/',views.logoutPatient, name="logout_p"),

    #doctor stuffs
    path('doc',views.DoctorIndexPage.as_view(), name="index_d"),
    path('logout/doctor/',views.logoutDoctor, name="logout_d"),
    path('dashboard/doctor/',views.DoctorDashboard.as_view(), name="dd"),
]
