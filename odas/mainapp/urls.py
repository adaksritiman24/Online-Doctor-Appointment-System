from django.urls import path
from . import views
urlpatterns = [
    path('dashboard/patient/',views.PatientDashboard.as_view(), name="pd"),
    path('',views.IndexPage.as_view(), name="index"),
    path('logout/patient/',views.logoutPatient, name="logout_p")
]
