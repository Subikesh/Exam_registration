from main.views import log_in
from . import views
from django.urls import path

app_name = 'main'

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("login/", views.log_in, name="log_in"),
    path("logout/", views.log_out, name="log_out"),
    path("register/", views.register, name="register"),

]
