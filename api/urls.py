from django.urls import path, include
from .views import (
    AnnonceListCreateAPIView,
    AnnonceRetrieveUpdateDestroyAPIView,
    )

urlpatterns = [
    path('', AnnonceListCreateAPIView.as_view(), name='annonce-list-create'),
    path('annoncesapi/<int:id>/', AnnonceRetrieveUpdateDestroyAPIView.as_view(), name='annonce-retrieve-update-destroy'),
]