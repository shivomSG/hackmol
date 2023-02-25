from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
<<<<<<< HEAD
    path('index/', views.index, name='index'),
=======
    path('home/', views.home, name='home-page'),
>>>>>>> 9030d35611f55e414e58caa2fc8ee1c33fd937a4
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
]