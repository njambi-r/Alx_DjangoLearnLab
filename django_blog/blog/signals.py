# https://dev.to/earthcomfy/django-user-profile-3hik 
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Profile

# Receiver function which will run every time a user is created 
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

""""
User is the sender which is responsible for making the notification.
post_save is the signal that is sent at the end of the save method.

In general, what the above code does is after the User model's save() 
method has finished executing, it sends a signal(post_save) to the 
receiver function (create_profile) then this function will receive 
the signal to create and save a profile instance for that user.

Next step is to connect the receivers in the ready() method of 
the app's configuration by importing the signals module. 
Open apps.py where we can include any application configuration 
for the users app.
"""