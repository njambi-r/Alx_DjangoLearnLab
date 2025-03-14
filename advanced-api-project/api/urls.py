from django.urls import path
from .views import ListView, DetailView, CreateView, UpdateView, DeleteView

#setup url patterns for the views
urlpatterns = [
    path('books/', ListView.as_view(), name='books-list'),
    path('books/<int:pk>/', DetailView.as_view(), name='books-retrieve'),
    path('books/create/', CreateView.as_view(), name='books-create'),
    path('books/update/<int:pk>/', UpdateView.as_view(), name='books-update'),
    path('books/delete/<int:pk>/', DeleteView.as_view(), name = "books-delete"),
]