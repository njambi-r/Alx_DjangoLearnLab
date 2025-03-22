from django import forms
from django.contrib.auth.models import User
from .models import Profile
#Forms
from django import forms
from django.forms import ModelForm
from .models import Post, Comment

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']

"""
Develop a form for the Post model using Django’s 
ModelForm to handle the creation and updating of 
blog posts. Ensure the form validates data properly 
and includes fields for title, content, and 
automatically set author based on the logged-in user.
"""
# Create form class
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "author"]

# Validate title
def clean_title(self):
    title = self.cleaned_data.get('title')
    if len(title) < 200:
        raise forms.ValidationError("The title cannot exceed 200 characers")
    return title

#Create comment form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content'] #Because all other fields don't require user input

    # Validate content field to ensure no blank comments
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) == 0:
            raise forms.ValidationError('Cannot post blank comment')
        return content




