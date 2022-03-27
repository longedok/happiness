from django.urls import path
from django.contrib.auth import views as auth_views

from server.core.views import words, scores, SignUpView, LogInView, SignUpSuccessView

urlpatterns = [
    path("", words, name="words"),
    path("scores", scores, name="scores"),
    path("signup", SignUpView.as_view(), name="signup"),
    path("signup_success", SignUpSuccessView.as_view(), name="signup-success"),
    path("login", LogInView.as_view(), name="login"),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
]
