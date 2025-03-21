from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, "blog/home.html")

# Create your views here.
def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        #Redirect to a success page.
    
    else:
        #Return an invalid login error message.

def logout_view(request):
    logout(request)
    #Redirect to a success page