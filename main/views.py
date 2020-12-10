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
    
    # Display all the subjects which are not registered before
    reg_subs = Register.objects.filter(Student = request.user).values('Subjects')
    display_subjects = Subject.objects.filter(Semester__lte = student.Semester).\
        filter(Department= student.Department).\
        exclude(pk__in= reg_subs)

    context['subjects'] = display_subjects
    context['user'] = request.user
    context['student'] = student
    
    if request.method == "POST":
        reg = Register(Student = request.user)
        subjects = request.POST.getlist('subject')
        subs = display_subjects.filter(Semester= student.Semester).filter(Department= student.Department)
        for sub in subs:
            subjects.append(sub.pk)
        if not subjects:
            messages.warning(request, "Please select atleast one subject.")
            return redirect("main:register")
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

    # Subjects which are not selected for this registration
    reg_subs = Register.objects.filter(Student = request.user).values('Subjects')
    subs = Subject.objects.filter(Semester__lte = student.Semester).\
        filter(Department= student.Department).\
        exclude(pk__in= reg_subs).\
        exclude(pk__in= reg.Subjects.all())
    context['non_reg_subs'] = subs
    return render(request, 'summary.html', context)

def payment(request, reg_id, paid):
    context = {"paid": paid}    
    if paid == 1:
        register = get_object_or_404(Register, pk= reg_id)
        register.Paid = True

        for subject in register.Subjects.all():
            attempt = Subject_attempts.objects.filter(Student=request.user).get(Sub_code=subject.Sub_code)
            # Increment an attempt for the student on that subject
            attempt.attempts += 1
        register.save()
        context['register'] = register
        return render(request, 'bank.html', context)
    elif paid == 2:
        return render(request, "payment.html")
    messages.error(request, "Your registration is cancelled. You can continue payment from profile.")
    return redirect("main:profile")

def del_reg(request, reg_id):
    regn = get_object_or_404(Register, pk = reg_id)
    regn.delete()
    return redirect("main:profile")
    