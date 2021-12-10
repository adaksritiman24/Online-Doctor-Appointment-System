from django.urls import path
from . import views

urlpatterns = [
    path("chatwindow/appointmentcall/<int:room_name>/",views.main_view, name = "main-chat-view"),
]