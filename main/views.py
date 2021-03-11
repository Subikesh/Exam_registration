from django.contrib.auth.models import User, auth
from django.contrib import messages
from main.models import Student, Subject, Subject_attempts, Register
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.views import generic
from django.views.generic.edit import CreateView
from .forms import RegisterForm

def homepage(request):
    context = {"home":"active"}

    # Department filter
    dep = request.GET.get('dept', "CSE")
    subjects = Subject.objects.filter(Department = dep)
    context['dept'] = dep

    # Semester filter
    sem = request.GET.get('sem', 0)
    if int(sem) != 0:
        subjects = subjects.filter(Semester = sem)
        context['sem'] = sem
    
    # Subject name filter
    name = request.GET.get('name', '')
    if name:
        print(name)
        subjects = subjects.filter(Q(Name__icontains = name) | Q(Sub_code__icontains = name))
        context['search'] = name

    sem_list = []
    for i in range(1, 9):
        subs = subjects.filter(Semester= i)
        sem_list.append(subs)
    context['sem_list'] = sem_list
    
    context['subjects'] = subjects
    return render(request, "main/home.html", context)

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
            return HttpResponseRedirect(reverse('main:homepage'))
        else:
            messages.error(request, "Username or Password is incorrect.")
    return render(request, 'main/login.html', context)

# Logout the current user
def log_out(request):
    auth.logout(request)
    messages.info(request, "You have been logged out of the website.")
    return HttpResponseRedirect(reverse('main:log_in'))

class profile(generic.DetailView):
    model = User
    template_name = 'main/profile.html'

    # Replacing user pk with request.user
    def get_object(self):
        return self.request.user

    # Add extra context as active for navbar
    def get_context_data(self, **kwargs):
        context = super(profile, self).get_context_data(**kwargs)
        context['profile'] = 'active'
        return context

# def register(request):
#     context = {'registerPage': 'active'}
#     total_fee = 0
#     student = request.user.student
    
#     # Display all the subjects which are not registered before
#     reg_subs = request.user.registrations.values('Subjects')
#     display_subjects = Subject.objects.filter(Semester__lte = student.Semester).\
#         filter(Department= student.Department).\
#         exclude(pk__in= reg_subs).\
#         exclude(Sub_code__in = Subject_attempts.objects.\
#             filter(Student = request.user).\
#             filter(Passed = True).values('Sub_code'))

#     context['subjects'] = display_subjects
#     context['user'] = request.user
#     context['student'] = student
    
#     if request.method == "POST":
#         reg = Register(Student = request.user)
#         subjects = request.POST.getlist('subject')
#         subs = display_subjects.filter(Semester= student.Semester).filter(Department= student.Department)
#         for sub in subs:
#             subjects.append(sub.pk)
#         if not subjects:
#             messages.warning(request, "Please select atleast one subject.")
#             return HttpResponseRedirect(reverse("main:register"))
#         reg.save()
#         for s in subjects:
#             subject = Subject.objects.get(pk=s)
#             # Checking the maximum attempts for that subject
#             try:
#                 attempt = Subject_attempts.objects.filter(Student=request.user).get(Sub_code=subject.Sub_code)
#             except Subject_attempts.DoesNotExist:
#                 attempt = Subject_attempts(Student = request.user, Sub_code = subject.Sub_code, attempts = 0)
#                 attempt.save()
#             if attempt.attempts > 4 and not attempt.Passed:
#                 messages.error(f"You have reached the maximum attempts for {subject}.")
#                 break
#             reg.Subjects.add(subject)
#             total_fee += subject.Fee
#         reg.TotalFee = total_fee
#         reg.save()
#         return HttpResponseRedirect(reverse("main:summary", args=[reg.pk,]))
#     return render(request, 'main/register.html', context)

# Register subjects 
class Register(CreateView):
    model = Register
    template_name = 'main/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('main:homepage')

    def get_form_kwargs(self):
        # send the current user instance to the RegisterForm kwargs
        kwargs = super(Register, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(Register, self).get_context_data(**kwargs)
        context['register'] = 'active'
        context['user'] = self.request.user
        return context

    def get_success_url(self):
        return reverse('main:summary', args=[self.pk,])

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
        exclude(Sub_code__in = Subject_attempts.objects.\
            filter(Student = request.user).\
            filter(Passed = True).values('Sub_code')).\
        exclude(pk__in= reg.Subjects.all())
    context['non_reg_subs'] = subs
    return render(request, 'main/summary.html', context)

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
        return render(request, 'main/bank.html', context)
    elif paid == 2:
        return render(request, "main/payment.html")
    messages.error(request, "Your registration is cancelled. You can continue payment from profile.")
    return HttpResponseRedirect(reverse("main:profile"))
    return HttpResponseRedirect(reverse("main:profile"))

def del_reg(request, reg_id):
    regn = get_object_or_404(Register, pk = reg_id)
    regn.delete()
    return HttpResponseRedirect(reverse("main:profile"))
