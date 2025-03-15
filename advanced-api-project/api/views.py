from django.shortcuts import render
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.generics import (ListAPIView,
                                     CreateAPIView,
                                     RetrieveAPIView,
                                     UpdateAPIView,
                                     DestroyAPIView,
                                     )
from .models import Book, Author
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


# Create your views here.
# Generic views on book model to handle CRUD operations

# Retrieve all books
class ListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Restrict to read only for unauthenticated users 
    permission_classes = [IsAuthenticatedOrReadOnly] 


# Retrieve a single book
class DetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Restrict to read only for unauthenticated users only
    permission_classes = [IsAuthenticatedOrReadOnly]


# Add a new book
class CreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # Restrict to authenticated users only

# Modify an existing view
class UpdateView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer 
    permission_classes = [IsAuthenticated] # Restrict to authenticated users only

# Remove a book
class DeleteView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Restrict to authenticated users only