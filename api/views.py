from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from annonces.models import Annonce
from .serializers import ItemSerialzer

class AnnonceListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Annonce.objects.all()
    serializer_class = ItemSerialzer

class AnnonceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Annonce.objects.all()
    serializer_class = ItemSerialzer
    lookup_field = 'id'


