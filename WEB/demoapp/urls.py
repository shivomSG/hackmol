from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('index/', views.index, name='index'),
 #   path('home/', views.home, name='home-page'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('appointments/', views.appointments, name='appointments')
]