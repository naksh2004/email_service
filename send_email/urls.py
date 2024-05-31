# urls.py (main URL configuration file)

from django.urls import path, include  # Import include function
from mailsend import urls as mailsend_urls  # Import the app's URL configuration module

urlpatterns = [
    # Other URL patterns if any
    path('', include(mailsend_urls)),  # Include the app's URL configuration
]
