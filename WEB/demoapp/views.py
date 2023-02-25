from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as lg
from .models import patient_data

# Create your views here.

def index(request):
    return render(request, 'index.html')
def index1(request):
    return render(request, 'index.jsp')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return HttpResponse("Your password and confirm password are not Same!!")
            return redirect('signup')

        else:
            my_user = User.objects.create_user(username, email, password1)
            my_user.save()
            return redirect('login')

    return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            lg(request, user)
            return redirect('index1')
        else:
            return render(request,'login.html')

    return render(request,'login.html')

def beds(request):
    return render(request, 'beds.html')
def appointments(request):
        if request.method == 'POST':
          name = request.POST.get('name')
          age = request.POST.get('age')
          gender = request.POST.get('gender')
          doctor = request.POST.get('doctor')
          date = request.POST.get('time')
          pat_data = patient_data(name=name, age=age,  gender=gender, doctor=doctor, date=date)
          pat_data.save()
          print(name, age, doctor, date, gender)

        return render(request,'appointments.html')