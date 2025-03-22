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

# Connecting class-based views to allow CRUD actions
from .views import PostListView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView
urlpatterns += [
    path("posts/", PostListView.as_view(), name="post-list"),
    path("posts/new/", PostCreateView.as_view(), name="post-create"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/<int:pk>/edit/", PostUpdateView.as_view(), name="post-edit"),
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
]
