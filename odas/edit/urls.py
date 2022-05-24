from django.urls import path
from . import views
urlpatterns = [
    path('patient/', views.PatientEditPage.as_view(), name = "p_edit" ),
    path('doctor/', views.DoctorEditPage.as_view(), name = "d_edit" ),
    path('patient/reports/<int:rep_no>', views.viewReport, name = "vr" ),
    path('patient/reportsdelete/<int:rep_id>', views.delete_report, name = "del_rep" ),
]