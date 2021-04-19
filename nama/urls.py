from django.urls import path, include
from .views import namaView


urlpatterns = [
    path('', namaView.as_view())
]