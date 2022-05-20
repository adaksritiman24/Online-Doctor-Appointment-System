from django.urls import path
from . import views

urlpatterns=[
    path('upload/', views.UploadPage.as_view(), name='upload_article'),
    path('read/<int:id>', views.read, name='read_article'),
    path('home/',views.home, name='articleshome'),
    path('results/', views.results, name='results'),
    path('search/', views.search, name='search'),
]