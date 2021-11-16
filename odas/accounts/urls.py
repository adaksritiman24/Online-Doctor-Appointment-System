from django.urls import path
from . import views
urlpatterns = [
    path('register/patient/',views.PatientRegistration.as_view(), name="pr"),
    path('login/patient/',views.PatientLogin.as_view(), name="pl"),
]
