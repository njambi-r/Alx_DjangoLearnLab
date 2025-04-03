from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.ReadOnlyField(source='actor.username')
    target_type = serializers.SerializerMethodField()
    target_id = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'actor', 'verb', 'target_type', 'target_id', 'timestamp', 'is_read']

    def get_target_type(self, obj):
        return obj.content_type.model if obj.content_type else None

    def get_target_id(self, obj):
        return obj.object_id if obj.object_id else None

"""
Chatgpt
Incorrect target Representation in Serializer
target.id might not always be valid, as target is a GenericForeignKey.
Fix: Instead of target.id, provide target details dynamically.
"""