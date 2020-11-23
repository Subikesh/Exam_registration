from django.db import models
from django.db.models.fields import DateField, EmailField, FloatField
from django.db.models.fields.related import ForeignKey, ManyToManyField, OneToOneField

# Contains details of students
class Student(models.Model):
    GENDER_CHOICE = [('Male', 'Male'), ('Female', 'Female')]

    St_id = models.CharField(max_length=20, primary_key=True)
    St_name = models.CharField(max_length=100)
    DOB = models.DateField()
    Gender = models.CharField(max_length=7, choices=GENDER_CHOICE, null=True)
    Qualification = models.CharField(max_length=30)
    Semester = models.IntegerField()
    Email = models.EmailField()

# Stores objects for number of attempts done on each subjects
class Subject_attempts(models.Model):
    Student = ForeignKey(Student, on_delete=models.CASCADE)
    Sub_code = models.CharField(max_length=10)
    attempts = models.IntegerField(default=0)

class Register(models.Model):
    Student = ForeignKey(Student, on_delete=models.CASCADE)
    RegDate = DateField(auto_now_add=True)
    TotalFee = FloatField()

class Subject(models.Model):
    Name = models.CharField(max_length=70)
    Registration = ManyToManyField(Register)
    Duration = models.IntegerField()
    DateofExam = models.DateField()
    Fee = models.FloatField()