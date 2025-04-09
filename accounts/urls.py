# accounts/urls.py
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import UserRegisterView, ProfileView

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path(
        "login/", LoginView.as_view(template_name="accounts/login.html"), name="login"
    ),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
    path("profile/", ProfileView.as_view(), name="profile"),
]
