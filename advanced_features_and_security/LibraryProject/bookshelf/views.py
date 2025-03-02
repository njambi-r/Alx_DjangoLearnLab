from django.shortcuts import render
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Book
from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseForbidden
from .forms import BookForm
from .forms import ExampleForm

# Create your views here.

#Creating groups and assigning permissions
def create_groups():
    content_type = ContentType.objects.get_for_model(Book)
    permissions = {
        "can_view": "Can view book",
        "can_create": "Can create book",
        "can_edit": "Can edit book",
        "can_delete": "Can delete book",
    }

    groups_permissions = {
        "Viewers": ["can_view"],
        "Editors": ["can_view", "can_edit", "can_create"],
        "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
    }

    for group_name, perms in groups_permissions.items():
        group, created = Group.objects.get_or_create(name=group_name)
        for perm_codename in perms:
            permission = Permission.objects.get(codename=perm_codename, content_type=content_type)
            group.permissions.add(permission)
        group.save() 
        """
        Permission.objects.get(codename=perm_codename) retrieves the permission from the database.
        group.permissions.add(permission) assigns it to the group.

        To create the groups, we run the below function in Django shell:
        python manage.py shell
        >>> from bookshelf.views import create_groups
        >>> create_groups()
        """  
# ---------------------------------------------         
#using permission_required decorator to enforce permissions

# 1. View Book - Requires 'can_view' permission
@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book': book})

# 2. Create Book - Requires 'can_create' permission
@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        publication_year = request.POST.get('publication_year')

    if title and author and publication_year.isdigit():
        book = Book.objects.create(
            title=title,
            author=author,
            publication_year=int(publication_year),
            added_by=request.user
        )
        return redirect('view_book', book_id=book.id)
    
    return render(request, 'book_form.html')

# 3. Edit Book - Requires 'can_edit' permission
@login_required
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    # Ensure only the user who added the book or an admin can edit
    if request.user != book.added_by and not request.user.has_perm('bookshelf.can_edit'):
        return HttpResponseForbidden("You do not have permission to edit this book.")

    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        publication_year = request.POST.get('publication_year')

        if publication_year.isdigit():
            book.publication_year = int(publication_year)

        book.save()
        return redirect('view_book', book_id=book.id)
    
    return render(request, 'book_form.html', {'book': book})

# 4. Delete Book - Requires 'can_delete' permission
@login_required
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    # Ensure only the user who added the book or an admin can delete
    if request.user != book.added_by and not request.user.has_perm('bookshelf.can_delete'):
        return HttpResponseForbidden("You do not have permission to delete this book.")

    if request.method == 'POST':
        book.delete()
        return redirect('book_list')

    return render(request, 'book_confirm_delete.html', {'book': book})

#-------------------------
#Securely add books using Django Forms

def add_book(request):
    """
    View for adding a book securely using Django forms.
    Prevents SQL injection by using Django ORM.
    """
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()  # Securely saves data
            return redirect('book_list')  # Redirects to the book list page
    else:
        form = BookForm()

    return render(request, "bookshelf/form_example.html", {"form": form})

def example_view(request):
    """
    Example view demonstrating secure form handling.
    """
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the valid form data (e.g., save to DB or send an email)
            return render(request, "bookshelf/example_success.html")  # Redirect or show success page
    else:
        form = ExampleForm()

    return render(request, "bookshelf/example_form.html", {"form": form})
