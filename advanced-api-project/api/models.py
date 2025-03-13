from django.db import models

# Create your models here.
# Author model
class Author(models.Model):
    name = models.CharField(max_length=250)

# Book model
class Book(models.Model):
    title = models.CharField(max_length=400)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)



