from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username=username).exists():
            messages.info(request, "Invalid Username")
            return redirect("/login/")
        user = authenticate(username=username, password=password)
        if user is None:
            messages.info(request, "Invalid Password")
            return redirect("/login/")
        else:
            login(request, user)
            return redirect("/")
    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect("/")

def signup(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request, "Username already taken")
            return redirect("/signup/")
        else:
            User.objects.create_user(
                first_name=first_name,
                email=email,
                username=username,
                password=password
            )
            messages.info(request, "Account Created Successfully")
            return redirect("/signup/")
    return render(request, 'signup.html')
