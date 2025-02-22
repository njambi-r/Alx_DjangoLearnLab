from relationship_app.models import Author, Book, Library, Librarian

#Query all books by a specific author.
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return [book.title for book in books]
    except Author.DoesNotExist:
        return f"No author with the name {author_name}"
    

#List all books in a library.
def list_all_books(library_name):
    try:
         library = Library.objects.get(name=library_name)
         books = library.books.all()
         return [book.title for book in books]
    except Library.DoesNotExist:
        return f"{library_name} does not exist"
    
#Retrieve the librarian for a library.
def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.objects.get(library=library)
        return librarian.name
    except Library.DoesNotExist:
        return f"Librarian for {library_name} not found"