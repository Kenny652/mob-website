from django.urls import path
from .views import (
    AnnonceCreateView,
    AnnonceListView,
    AnnonceUpdateView,
    AnnonceDetailView,
    AnnonceDeleteView,
    accueil
)

app_name = 'annonces'
urlpatterns = [
    path('', accueil, name='annonce-accueil'),
    path('list/', AnnonceListView.as_view(), name='annonce-list'),
    path('create/', AnnonceCreateView.as_view(), name='annonce-create'),
    path('<int:id>/', AnnonceDetailView.as_view(), name='annonce-detail'),
    path('<int:id>/update/', AnnonceUpdateView.as_view(), name='annonce-update'),
    path('<int:id>/delete/', AnnonceDeleteView.as_view(), name='annonce-delete')
]
