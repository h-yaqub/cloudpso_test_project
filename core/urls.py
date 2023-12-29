from django.urls import path

from . import views

urlpatterns = [
    path("accounts/register/", views.RegisterView.as_view(), name="register"),
    path("", views.HomeView.as_view(), name="home"),
]
