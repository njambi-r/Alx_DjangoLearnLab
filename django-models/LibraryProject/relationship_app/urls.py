from django.urls import path
from .views import book_list, library_book_view

app_name = "relationship_app"

urlpatterns = [
    path("books/", book_list, name="book-list"),  # Function-Based View
    path("library/<int:pk>/", library_book_view.as_view(), name="library-book-detail"),  # Class-Based View
]
