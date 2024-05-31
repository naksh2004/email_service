# urls.py

from django.urls import path
from .views import my_view

urlpatterns = [
    path('send/', my_view, name='send'),
]
