from django.forms.models import model_to_dict
book = Book.objects.get(id=2)
print(model_to_dict(book))
#output: {'id': 2, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1949}