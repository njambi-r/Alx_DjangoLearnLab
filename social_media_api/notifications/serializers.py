from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.ReadOnlyField(source='actor.username')
    target = serializers.ReadOnlyField(source='target.id')

    class Meta:
        model = Notification
        fields = '__all__'
