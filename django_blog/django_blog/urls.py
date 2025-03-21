"""
URL configuration for django_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("admin/", admin.site.urls),

    # Include Django's built-in authentication URLs
    path("accounts/", include("django.contrib.auth.urls")),  

    # Custom authentication-related views
    path("accounts/register/", include("blog.urls")),  # Register and profile are in blog.urls

    # Explicit login/logout URLs (optional, but avoid duplication)
    path("accounts/login/", auth_views.LoginView.as_view(template_name="registration/login.html")),
    #path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),

    # Home page
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)