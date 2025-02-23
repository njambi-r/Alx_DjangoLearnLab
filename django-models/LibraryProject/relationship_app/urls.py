from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView #login view
from django.contrib.auth.views import LogoutView #logout view
from . import views


app_name = "relationship_app"

urlpatterns = [
    path("books/", list_books, name="book-list"),  # Function-Based View
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library-book-detail"),  # Class-Based View
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'), #login
    path("logout/", LogoutView.as_view(template_name="registration/logout.html"), name="logout"),#logout
    path("register/", views.register, name="register"),  # Explicitly include views.register
    path("admin-view/", views.admin_view, name="admin-view"),
    path("librarian-view/", views.librarian_view, name="librarian-view"),
    path("member-view/", views.member_view, name="member-view"),
    path("books/add/", views.add_book, name="add-book"),
    path("books/edit/<int:book_id>/", views.edit_book, name="edit-book"),
    path("books/delete/<int:book_id>/", views.delete_book, name="delete-book"),
]
