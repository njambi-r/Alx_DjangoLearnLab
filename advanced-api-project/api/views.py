from django.shortcuts import render
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.generics import (ListAPIView,
                                     CreateAPIView,
                                     RetrieveAPIView,
                                     UpdateAPIView,
                                     DestroyAPIView,
                                     )
from .models import Book, Author


# Create your views here.
# Generic views on book model to handle CRUD operations

# Retrieve all books
class ListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Retrieve a single book
class DetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Add a new book
class CreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Modify an existing view
class UpdateView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer  

# Remove a book
class DeleteView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer  