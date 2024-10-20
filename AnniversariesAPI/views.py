from django.shortcuts import render

from rest_framework import generics
from .models import Anniversary
from .serializers import AnniversarySerializer


# List all anniversaries and create a new one
class AnniversaryListCreateView(generics.ListCreateAPIView):
    queryset = Anniversary.objects.all()
    serializer_class = AnniversarySerializer


# Retrieve, update, and delete a specific anniversary by ID
class AnniversaryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Anniversary.objects.all()
    serializer_class = AnniversarySerializer
