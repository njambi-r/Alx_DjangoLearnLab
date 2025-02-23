from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
#user registration
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
#user login
from django.contrib.auth import login


#1. Setting up template views
# Create your views here.
#function-based view
def list_books(request):
    books = Book.objects.all()
    context = {"books": books}
    return render (request, 'relationship_app/list_books.html', context)

#class-based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) #get default context data
        return context

#2: Setting up user authentication views
# User Registration
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


