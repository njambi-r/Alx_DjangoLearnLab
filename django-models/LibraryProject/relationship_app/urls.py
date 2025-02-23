from django.urls import path
from .views import list_books, LibraryDetailView

app_name = "relationship_app"

urlpatterns = [
    path("books/", list_books, name="book-list"),  # Function-Based View
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library-book-detail"),  # Class-Based View
]
