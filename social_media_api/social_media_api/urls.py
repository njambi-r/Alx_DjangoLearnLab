from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')), # user authentication
    path('api-auth/', include('rest_framework.urls')),  # Optional: Browsable API login/logout
    path('api/', include('posts.urls')),  # Posts & comments API
]
