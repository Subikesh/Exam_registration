from django.shortcuts import render, redirect, get_object_or_404
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
            return redirect('main:homepage')
        else:
            messages.error(request, "Username or Password is incorrect.")
    return render(request, 'login.html', context)

# Logout the current user
def log_out(request):
    auth.logout(request)
    messages.info(request, "You have been logged out of the website.")
    return redirect('main:log_in')

def profile(request):
    context= {'profile': 'active'}
    user =  request.user
    context['user'] = user 
    student = Student.objects.get(user= user)    
    context['student'] = student
    reg = Register.objects.filter(Student= user)
    context['registrations'] = reg
    return render(request, 'profile.html', context)

def register(request):
    context = {'registerPage': 'active'}
    total_fee = 0
    student = Student.objects.get(user=request.user)
    display_subjects = Subject.objects.filter(Semester__lte = student.Semester).filter(Department= student.Department)
    context['subjects'] = display_subjects
    context['user'] = request.user
    context['student'] = student
    
    if request.method == "POST":
        reg = Register(Student = request.user)
        subjects = request.POST.getlist('subject')
        subs = Subject.objects.filter(Semester= student.Semester).filter(Department= student.Department)
        for sub in subs:
            subjects.append(sub.pk)
        reg.save()
        for s in subjects:
            subject = Subject.objects.get(pk=s)
            # Checking the maximum attempts for that subject
            try:
                attempt = Subject_attempts.objects.filter(Student=request.user).get(Sub_code=subject.Sub_code)
            except Subject_attempts.DoesNotExist:
                attempt = Subject_attempts(Student = request.user, Sub_code = subject.Sub_code, attempts = 0)
                attempt.save()
            if attempt.attempts > 4 and not attempt.Passed:
                messages.error(f"You have reached the maximum attempts for {subject}.")
                break
            reg.Subjects.add(subject)
            total_fee += subject.Fee
        reg.TotalFee = total_fee
        reg.save()
        return redirect(f'/register_summary/{reg.pk}')
    return render(request, 'register.html', context)

def register_summary(request, reg_id):
    context = {'registerPage': 'active'}
    student = Student.objects.get(user=request.user)
    reg = get_object_or_404(Register, pk= reg_id)
    context['register'] = reg
    context['student'] = student
    return render(request, 'summary.html', context)

def payment(request, reg_id, payed):    
    register = get_object_or_404(Register, pk= reg_id)
    if payed == 1:
        register.Payed = True

        for subject in register.Subjects.all():
            attempt = Subject_attempts.objects.filter(Student=request.user).get(Sub_code=subject.Sub_code)
            # Increment an attempt for the student on that subject
            attempt.attempts += 1
        messages.success(request, "Registration Successful")
        register.save()
        return redirect('main:homepage')
    else:
        messages.error(request, "Payment failed. Try again later.")
        return redirect('/profile/')