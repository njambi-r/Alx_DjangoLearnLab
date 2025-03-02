from django.forms.models import model_to_dict
from bookshelf.models import Book
book = Book.objects.get(id = 2)
book.delete()
#output (1, {'bookshelf.Book': 1})