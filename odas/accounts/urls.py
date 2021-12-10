from django.urls import path
from . import views
urlpatterns = [
    path('register/patient/',views.PatientRegistration.as_view(), name="pr"),
    path('register/doctor/',views.DoctorRegistration.as_view(), name="dr"),

    path('login/patient/',views.PatientLogin.as_view(), name="pl"),
    path('login/doctor/',views.DoctorLogin.as_view(), name="dl"),
]
