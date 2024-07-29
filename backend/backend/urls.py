
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin_secret_url/', admin.site.urls),
    path('',include('api.urls')),
    path('', include('django.contrib.auth.urls')),
]
