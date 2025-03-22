from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .views import PostListView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView
from .views import CommentAddView, CommentDeleteView, CommentUpdateView

urlpatterns = [
   path("register/", views.RegistrationView.as_view(), name="register"),  
   path("profile/", views.profile, name="profile"),

   # Explicit login/logout URLs (optional, but avoid duplication)
   path("login/", auth_views.LoginView.as_view(template_name="registration/login.html")),
   #path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),  
]

# Connecting class-based views to allow CRUD actions
urlpatterns += [
    path("post/", PostListView.as_view(), name="post-list"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
]

#adding comments views
urlpatterns += [
    path("posts/<int:post_id>/comments/new/", CommentAddView, name="add_comment"),
    path("comments/<int:pk>/update/", CommentUpdateView.as_view(), name="comment_update"),
    path("comments/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment_delete"),
]