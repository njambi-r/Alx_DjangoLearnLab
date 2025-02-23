from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView

# Create your views here.
#function-based view
def book_list(request):
    books = Book.objects.all()
    context = {"books": books}
    return render (request, 'relationship_app/list_books.html', context)

#class-based view
class library_book_view(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) #get default context data
        return context
