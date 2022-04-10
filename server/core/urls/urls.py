from django.contrib.auth import views as auth_views
from django.urls import path

from server.core.views import LogInView, SignUpSuccessView, SignUpView, scores, words

urlpatterns = [
    path("", words, name="words"),
    path("scores", scores, name="scores"),
    path("signup", SignUpView.as_view(), name="signup"),
    path("signup_success", SignUpSuccessView.as_view(), name="signup-success"),
    path("login", LogInView.as_view(), name="login"),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
]
