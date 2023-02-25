from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name='home-page'),
    path('login/', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
]