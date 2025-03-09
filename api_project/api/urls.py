from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename = 'book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view

    #include router urls for BookViewSet (all CRUD operations)
    path('', include(router.urls)), #includes all routes registered with the router
]

# REST framework has a built-in view that allows users to obtain a token given a 
# username and a password.
# This can be done using DRF’s built-in views like obtain_auth_token.
urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token)
]