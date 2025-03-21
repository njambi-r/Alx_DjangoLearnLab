from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
   # path("", views.home, name="home"),  
   path("register/", views.RegistrationView.as_view(), name="register"),  
   # path("accounts/login/", views.custom_login, name="login"),  
   # path("accounts/register/", views.register, name="register"),  
]