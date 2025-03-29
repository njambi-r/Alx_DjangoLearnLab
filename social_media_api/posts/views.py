from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import PostSerializer, CommentSerializer
from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model

# Create your views here.
# using REST framework viewsets which encapsulate the logic for common CRUD operations on models

class PostViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    """
    https://www.django-rest-framework.org/api-guide/permissions/#isauthenticatedorreadonly 
    Allow read permissions to anonymous users, and only allow 
    write permissions to authenticated users.
    """

    def perform_create(self, serializer):
        serializer.save(author=self.request.user) 
    """
    https://stackoverflow.com/questions/41094013/when-to-use-serializers-create-and-modelviewsets-perform-create
    perform_create is used when you want to supply 
    extra data before save (like serializer.save(owner=self.request.user) 
    """