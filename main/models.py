from django.db import models
from django.contrib.auth.models import User

# Contains details of students
class Student(models.Model):
    GENDER_CHOICE = [('Male', 'Male'), ('Female', 'Female')]

    # Extending the user model to add additional details of students
    user =  models.OneToOneField(User, on_delete=models.CASCADE)    
    DOB = models.DateField()
    Gender = models.CharField(max_length=7, choices=GENDER_CHOICE, null=True)
    Qualification = models.CharField(max_length=30, null=True)
    Semester = models.IntegerField()

# Stores objects for number of attempts done on each subjects
class Subject_attempts(models.Model):
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Sub_code = models.CharField(max_length=10)
    attempts = models.IntegerField(default=0)

class Register(models.Model):
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    RegDate = models.DateField(auto_now_add=True)
    TotalFee = models.FloatField(null=True)

class Subject(models.Model):
    Name = models.CharField(max_length=70)
    Registration = models.ManyToManyField(Register)
    Duration = models.IntegerField(default=180)
    DateofExam = models.DateField()
    Fee = models.FloatField()