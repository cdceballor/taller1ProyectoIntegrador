from django.shortcuts import render
from rest_framework import viewsets
from .models import Temperatura
from .Serializers import TemperaturaSerializer

class TemperaturaViewSet(viewsets.ModelViewSet):
    queryset = Temperatura.objects.all().order_by('-created')
    serializer_class = TemperaturaSerializer
# Create your views here.
