
from django.contrib import admin
from django.urls import path
from .views import index, profile

urlpatterns = [
    path('', index, name='index') ,
    path('<str:username>/', profile, name='profile')
] 
