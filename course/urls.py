from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [

    path('course/', views.studentInfo),
    path('aaa/', views.showformloop),
    
    
]
