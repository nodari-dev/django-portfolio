from django.urls import path
from .views import message_create
urlpatterns = [
    path('contact/', message_create, name="test"),
]

