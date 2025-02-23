from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView #login view
from django.contrib.auth.views import LogoutView #logout view

app_name = "relationship_app"

urlpatterns = [
    path("books/", list_books, name="book-list"),  # Function-Based View
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library-book-detail"),  # Class-Based View
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'), #login
    path("logout/", LogoutView.as_view(template_name="registration/logout.html"), name="logout"),#logout
]
