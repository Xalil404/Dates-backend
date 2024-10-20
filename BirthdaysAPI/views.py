from django.shortcuts import render

from rest_framework import generics
from .models import Birthday
from .serializers import BirthdaySerializer


# List all birthdays or create a new birthday
class BirthdayListCreateView(generics.ListCreateAPIView):
    queryset = Birthday.objects.all()
    serializer_class = BirthdaySerializer


# Retrieve, update, or delete a specific birthday by ID
class BirthdayRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Birthday.objects.all()
    serializer_class = BirthdaySerializer
