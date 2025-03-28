from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import PostSerializer, CommentSerializer
from rest_framework import viewsets, permissions
from .models import Post, Comment
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Create your views here.
# using REST framework viewsets which encapsulate the logic for common CRUD operations on models

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    """Add filtering"""
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'content']
    """Add search"""
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']    

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
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