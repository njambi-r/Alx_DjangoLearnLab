from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# Custom user model
class CustomUser(AbstractUser):
    bio = models.TextField(blank = True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    followers = models.ManyToManyField("self", symmetrical=False, related_name='following')
    """
    https://docs.djangoproject.com/en/5.1/ref/models/fields/#django.db.models.ManyToManyField.symmetrical:~:text=ManyToManyField.symmetrical
    ManyToManyField.symmetrical is used to define many to many relationship 
    on self. The manytomany foeld is assumed to be symmetrical.
    i.e, if I am your friend, then you're my friend. 
    Set symmetrical to False if you don't want symmetry.
    """