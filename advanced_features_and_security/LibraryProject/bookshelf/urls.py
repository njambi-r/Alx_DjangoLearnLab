from django.urls import path
from .views import view_book, create_book, edit_book, delete_book, example_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('books/', view_book, name='book_list'),
    path('books/<int:book_id>/', view_book, name='view_book'),
    path('books/create/', create_book, name='create_book'),
    path('books/<int:book_id>/edit/', edit_book, name='edit_book'),
    path('books/<int:book_id>/delete/', delete_book, name='delete_book'),
    path('example/', example_view, name='example_form'),

    # Authentication URLs (if needed)
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
