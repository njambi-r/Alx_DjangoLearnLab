from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
   path("register/", views.RegistrationView.as_view(), name="register"),  
   path("profile/", views.profile, name="profile"),  
]