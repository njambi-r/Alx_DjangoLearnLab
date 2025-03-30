from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class Notification(models.Model):
    recipient = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='notifications')
    actor = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    verb = models.CharField(max_length=250)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    target = GenericForeignKey("content_type", "object_id")
    timestamp = models.DateTimeField(auto_now_add=True)
"""
https://docs.djangoproject.com/en/5.1/ref/contrib/contenttypes/#django.contrib.contenttypes.fields.GenericForeignKey 
ContentType allows your model to effectively tie itself to another model class
"""