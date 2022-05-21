from django.urls import path
from . import views

urlpatterns=[
    path('upload/', views.UploadPage.as_view(), name='upload_article'),
    path('read/<int:id>', views.read, name='read_article'),
    path('home/',views.home, name='articleshome'),
    path('results/', views.results, name='results'),
    path('search/', views.search, name='search'),

    #links
    path('a_dashboard/', views.dashboard, name='a_dashboard'),
    path('a_app/', views.app_page, name='a_app'),
    path('a_profile/', views.edit_profile, name='a_profile'),
    path('a_showhome/', views.show_home, name='a_showhome'),
]