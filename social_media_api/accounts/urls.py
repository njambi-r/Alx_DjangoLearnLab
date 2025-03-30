from django.urls import path
from .views import RegisterView, LoginView, ProfileView, FollowUserView, UnfollowUserView, IsFollowingView
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', ObtainAuthToken.as_view(), name='api-login'),
    path('profile/', ProfileView.as_view(), name='profile'),
]

#follow, unfollow, and view following
urlpatterns +=[
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow_user'),
    path('is_following/<int:user_id>/', IsFollowingView.as_view(), name='is_following'),
]