from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):  # Ensures "return self.name" is present
        return self.name

class Book(models.Model):
    title = models.CharField(max_length = 200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):  # Ensures "return self.name" is present
        return self.name

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def __str__(self):  # Ensures "return self.name" is present
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):  # Ensures "return self.name" is present
        return self.name

#Creating user profiles
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE )
    role = models.CharField(
        max_length=20,
        choices=[
            ('Admin', 'Admin'),
            ('Librarian', 'Librarian'),
            ('Member', 'Member'),
        ],
        default='Member'
    )  
   
    def __str__(self):
        return f"{self.user.username} - {self.role}"  


