from django.urls import path
from .views import NotificationListView, MarkNotificationReadView

urlpatterns = [
    path("notifications/", NotificationListView.as_view(), name="notifications-list"),
    path("<int:pk>/read/", MarkNotificationReadView.as_view(), name="mark-notification-read"),
]
