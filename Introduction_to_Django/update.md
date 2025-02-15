
x = Book.objects.all()[0]
x.title = 'Nineteen Eighty-Four'   
x.save()
Book.objects.all().values()
#output: <QuerySet [{'id': 1, 'title': 'Nineteen Eighty-Four', 'author': 'George Orwell', 'publication_year': 1949}]>