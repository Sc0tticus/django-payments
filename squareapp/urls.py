# square/urls.py

from django.urls import path
from .views import list_merchants

urlpatterns = [
    path('merchants/', list_merchants, name='list_merchants'),
]
