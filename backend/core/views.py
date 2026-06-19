from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import Sector
from .serializers import SectorSerializer


class SectorViewSet(viewsets.ModelViewSet):
    serializer_class = SectorSerializer
    queryset = Sector.objects.all()