from django.forms.models import model_to_dict
from bookshelf.models import Book
book = Book.objects.get(id=2)
book.title = 'Nineteen Eighty-Four' 
book.save()
print(model_to_dict(book))
#output {'id': 2, 'title': 'Nineteen Eighty-Four', 'author': 'George Orwell', 'publication_year': 1949}