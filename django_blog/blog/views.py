from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm

# Classbased views
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import PostForm

# Adding comment funtionality
from .models import Comment
from .forms import CommentForm

# Home page view
def home(request):
    return render(request, "blog/home.html")

# User registration
class RegistrationView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "blog/register.html"

# Profile view. Limits access to logged in users
@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'profile.html', context)

#--------
# CRUD class-based views setup
# List all posts
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"  # Variable used in the template

# Display details of a single blog post
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

# Allow authenticated user to add a new blog post
#Only logged-in users can access (LoginRequiredMixin)
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm 
    """
    The PostForm class defines what fields are included and how validation is performed.
    Validation Happens Automatically
    Django automatically runs field validation when the form is submitted.
    If the input is valid, the form_valid() method is executed.
    If invalid, Django reloads the form with error messages.
    """
    template_name = "blog/post_form.html"

    # Automatically assign logged-in user as author
    def form_valid(self, form):
        form.instance.author = self.request.user  
        return super().form_valid(form)

# Allow authors to edit their posts
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    # Only the author can edit the post
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  

# Allow authors to delete their posts
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("post-list")  # Redirect to post list page after deletion

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Only the author can delete the post

#-----
# CRUD operations for comments

# Allow authenticated users to post new comments 
@login_required #only authenticated users can add comments
def CommentAddView(request, post_id):
    post = get_object_or_404(Post, id=post_id) #retrieve blog post to be associated with comment, if it does not exist, return 404 error
    if request.method == "POST": #form submitted via post, meaning user is trying to create a new comment
        form = CommentForm(request.POST)
        if form.is_valid(): #Checks validation errors 
            comment = form.save(commit=False) #creates new comment object but does not save it yet
            comment.post = post #attach comment to specific post
            comment.author = request.user #currently logged in user set as comment author
            comment.save() #permanently save comment to the database
            return redirect("post_detail", pk=post.id) #after saving, user is redirected to the post detail page to see their comment
        else:
            form = CommentForm()
        return redirect ("post_detail", pk=post.id) #if form is invalid, we redirect back to the post detail page

# Alllow comment author to edit comment
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"

    #Ensure comment remains linked to the correct post
    def from_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    #Redirect user to post where comment was made
    def get_success_url(self):
        return self.object.post.get_absolute_url()
    
    #Ensure only comment author can edit
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

#Allow comment author to delete comment
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = "blog/comment_confirm_delete.html"

    #Redirect user to blog post page after deleting comment
    def get_success_url(self):
        return self.object.post.get_absolute_url()
    
    #Ensure only author can delete a comment
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
