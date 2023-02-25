from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name='home-page'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
]