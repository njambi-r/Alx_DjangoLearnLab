from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import PostSerializer, CommentSerializer
from rest_framework import viewsets, permissions
from .models import Post, Comment
from rest_framework import generics, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

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

# Feed functionality
class UserFeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    """get posts by followed users"""
    def get_queryset(self):
        following_users = self.request.user.following.all() #retrive all users the authenticated user follows
        return Post.objects.filter(author__in=following_users).order_by('-created_at') #retrieves posts by followed users and orders them by the most recent first
        
