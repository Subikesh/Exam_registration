from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from main.models import Student, Subject, Subject_attempts, Register

def homepage(request):
    context = {"home":"active"}
    return render(request, "home.html", context)

# Login for the username and password
def log_in(request):
    context = {'log_in':'active'}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are successfully logged in.")
            return redirect('/')
        else:
            messages.error(request, "Username or Password is incorrect.")
    return render(request, 'login.html', context)

# Logout the current user
def log_out(request):
    auth.logout(request)
    messages.info(request, "You have been logged out of the website.")
    return redirect('/')