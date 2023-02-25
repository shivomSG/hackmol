from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# Create your views here.

def home(request):
    return render(request, 'home.html')
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
            login(request, user)
            return redirect('index')
        else:
            return render(request,'login.html')




    return render(request,'login.html')