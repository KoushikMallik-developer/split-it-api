from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('expenses.urls')),
    path('', include('dashboard.urls')),
    path('home/', include('home.urls')),  # Add a new app for the homepage
]
