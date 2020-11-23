from django.shortcuts import render

# Create your views here.
def homepage(request):
    context = {"home":"active"}
    return render(request, "home.html", context)