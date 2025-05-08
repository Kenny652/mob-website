from rest_framework import serializers
from annonces.models import Annonce

class ItemSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Annonce
        fields = '__all__'