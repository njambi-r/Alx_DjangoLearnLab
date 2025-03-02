from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    """
    Form for adding and validating book data.
    """
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 3:
            raise forms.ValidationError("Title must be at least 3 characters long.")
        return title

    def clean_author(self):
        author = self.cleaned_data['author']
        if "<script>" in author:
            raise forms.ValidationError("Invalid characters detected.")
        return author

# ExampleForm: Demonstrating another secure form implementation
class ExampleForm(forms.Form):
    """
    Example form demonstrating secure user input handling.
    """
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def clean_name(self):
        name = self.cleaned_data['name']
        if not name.replace(" ", "").isalpha():  # Ensures name contains only letters
            raise forms.ValidationError("Name should contain only letters.")
        return name
