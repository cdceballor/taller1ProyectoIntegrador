from rest_framework import serializers
from .models import Temperatura

class TemperaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperatura
        fields = ('id', 'type', 'value', 'lati', 'longi', 'tipTerr')
