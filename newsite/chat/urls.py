from django.urls import path
from . import views

urlpatterns = [
    path("chatwindow/appointmentcall/",views.main_view, name = "main-view"),
    path("",views.index, name = "index"),
]