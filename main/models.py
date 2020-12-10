from django.db import models
from django.contrib.auth.models import User

# Contains details of students
class Student(models.Model):
    GENDER_CHOICE = [('Male', 'Male'), ('Female', 'Female')]
    DEPT_CHOICE = [('CSE', 'CSE'), ('Mechanical', 'Mech'), ('IT', 'IT'), ('ECE', 'ECE')]

    # Extending the user model to add additional details of students
    user =  models.OneToOneField(User, on_delete=models.CASCADE)
    DOB = models.DateField()
    Gender = models.CharField(max_length= 7, choices= GENDER_CHOICE, null=True)
    Department = models.CharField(max_length= 35, choices= DEPT_CHOICE)
    Semester = models.IntegerField()

    def __str__(self) -> str:
        return self.user.first_name

# Stores objects for number of attempts done on each subjects
class Subject_attempts(models.Model):
    Student = models.ForeignKey(User, on_delete=models.CASCADE)
    Sub_code = models.CharField(max_length=10)
    Passed = models.BooleanField(default= False)
    attempts = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.Student} {self.Sub_code}"

class Subject(models.Model):
    DEPT_CHOICE = [('CSE', 'CSE'), ('Mechanical', 'Mech'), ('IT', 'IT'), ('ECE', 'ECE')]

    Name = models.CharField(max_length=70)
    Sub_code = models.CharField(max_length=10)
    Department = models.CharField(max_length= 30, choices= DEPT_CHOICE)
    Semester = models.IntegerField()
    Duration = models.IntegerField(default=180)
    DateofExam = models.DateField()
    Fee = models.FloatField()

    def __str__(self) -> str:
        return self.Name

class Register(models.Model):
    Student = models.ForeignKey(User, on_delete=models.CASCADE)
    RegDate = models.DateField(auto_now_add=True)
    TotalFee = models.FloatField(null=True)
    Subjects = models.ManyToManyField(Subject)
    Paid = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.Student}, {self.pk}"