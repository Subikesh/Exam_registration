from django.contrib import admin
from .models import Student, Subject, Subject_attempts

# Register your models here.
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Subject_attempts)