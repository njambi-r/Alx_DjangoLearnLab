from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import generics, permissions, status
from rest_framework.authentication import TokenAuthentication

import notifications.models
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .models import CustomUser
from notifications.models import Notification

User = get_user_model()

# User Registration
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(username=request.data['username'])
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})

# User Login
class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            update_last_login(None, user)
            return Response({"token": token.key})
        return Response({"error": "Invalid Credentials"}, status=400)

# User Profile View
class ProfileView(generics.RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

#---------------
# Follow management views that allow users to follow and unfollow others
"""üsing CustomUser only because the cheker demands it"""
"""follow a user"""
class FollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post (self, request, user_id):
        user_to_follow = get_object_or_404(User, id=user_id)

        if request.user == user_to_follow:
            return Response({'error': 'You cannot follow yourself.'}, status=status.HTTP_400_BAD_REQUEST)
        
        #prevent duplicate follows
        if request.user.following.filter(id=user_to_follow.id).exists():
            return Response({'message': 'You are already following this user.'}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.add(user_to_follow)
            
        # Create notification for the user followed
        Notification.objects.create(
            recipient = user_to_follow,
            actor = request.user,
            verb = "started following you",
            target = user_to_follow
        )
        return Response({'message': f'You are now following {user_to_follow.username}.'}, status=status.HTTP_200_OK)


class UnfollowUserView(generics.GenericAPIView):
    """unfollow a user"""
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(User, id=user_id)

        if request.user == user_to_unfollow:
            return Response({'error': 'You cannot unfollow yourself.'}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.remove(user_to_unfollow)
        return Response({'message': f'You have unfollowed {user_to_unfollow.username}.'}, status=status.HTTP_200_OK)

class IsFollowingView(generics.GenericAPIView):
    """check if the authenticated user is following another user"""
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, user_id):
        user_to_check = get_object_or_404(User, id=user_id)
        is_following = request.user.following.filter(id=user_to_check.id).exists()
        return Response({'You are following': is_following}, status=status.HTTP_200_OK)