from django.shortcuts import render

from rest_framework import generics
from .models import Holiday
from .serializers import HolidaySerializer


# List all holidays and create a new one
class HolidayListCreateView(generics.ListCreateAPIView):
    queryset = Holiday.objects.all()
    serializer_class = HolidaySerializer

# Retrieve, update, and delete a specific holiday by ID
class HolidayDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Holiday.objects.all()
    serializer_class = HolidaySerializer
