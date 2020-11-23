from django.shortcuts import render

app_name = 'main'

def homepage(request):
    context = {"home":"active"}
    return render(request, "home.html", context)