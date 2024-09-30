from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.models import *
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout #login for storing session.
from django.contrib.auth.decorators import login_required
from django.conf import settings
import razorpay
import requests


def home(request):
    return render(request, 'index.html')


@login_required(login_url="/login/")
def job(request):
    jobs_from_database = Job.objects.all()
    return render(request, 'job.html', context={'job_list_all' : jobs_from_database})


@login_required(login_url="/login/")
def internship(request):
    jobs_from_database = Job.objects.all()
    return render(request, 'internship.html', context={'job_list_all' : jobs_from_database})


@login_required(login_url="/login/")
def contest(request):
    contests_from_database = Contest.objects.filter(Q(id__range=(1, 24)) | Q(id__range=(131, 206)))  # if we need multiple slices.
    return render(request, 'contest.html', context={'contest_list_all' : contests_from_database})


@login_required(login_url="/login/")
def news(request):
    news_from_database = News.objects.all()[107:122]
    context={'news_list_all' : news_from_database}
    return render(request, 'news.html', context)


def contact(request):
    if request.method == "POST":
        q_name = request.POST.get('q_name')
        q_email = request.POST.get('q_email')
        q_subject = request.POST.get('q_subject')
        q_message = request.POST.get('q_message')
        Contact.objects.create(
            q_name = q_name,
            q_email = q_email,
            q_subject = q_subject,
            q_message = q_message
            )
        messages.info(request, "Your Query Accepted, We will get back to you sortly.")
        return redirect("/contact/")
    return render(request, 'contact.html')



def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username = username).exists():
            messages.info(request, "Invalid Username")
            return redirect("/login/")
        user = authenticate(username = username, password = password)
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
        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(request, "Username already taken")
            # messages.warning(request, "Username already taken")
            return redirect("/signup/")
        else:
            User.objects.create_user(
                first_name = first_name,
                email = email,
                username = username,
                password=password
            )
            messages.info(request, "Account Created Successfully")
            return redirect("/signup/")
    return render(request, 'signup.html')

