from main.views import log_in
from . import views
from django.urls import path

app_name = 'main'

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("login/", views.log_in, name="log_in"),
    path("logout/", views.log_out, name="log_out"),
    path("register/", views.register, name="register"),
    path("register_summary/<int:reg_id>", views.register_summary, name="summary"),
    path("payment/<int:reg_id>/<int:paid>", views.payment, name="payment"),
    path("profile/", views.profile.as_view(), name="profile"),
    path("delete_regn/<int:reg_id>", views.del_reg, name="delete_regn"),
]
