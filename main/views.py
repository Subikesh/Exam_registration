from django.shortcuts import render

def homepage(request):
    context = {"home":"active"}
    return render(request, "home.html", context)