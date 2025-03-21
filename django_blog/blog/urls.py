from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
   path("register/", views.RegistrationView.as_view(), name="register"),  
   path("profile/", views.profile, name="profile"),

   # Explicit login/logout URLs (optional, but avoid duplication)
   path("login/", auth_views.LoginView.as_view(template_name="registration/login.html")),
   #path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),  
]