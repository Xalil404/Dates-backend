from django.shortcuts import render
from rest_framework import generics
from .models import Birthday
from .serializers import BirthdaySerializer


# List all birthdays for the authenticated user or create a new birthday
class BirthdayListCreateView(generics.ListCreateAPIView):
    serializer_class = BirthdaySerializer

    def get_queryset(self):
        # Only return birthdays for the authenticated user
        return Birthday.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Set the user to the authenticated user when creating a new birthday
        serializer.save(user=self.request.user)


# Retrieve, update, or delete a specific birthday by ID
class BirthdayRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BirthdaySerializer

    def get_queryset(self):
        # Only return birthdays for the authenticated user
        return Birthday.objects.filter(user=self.request.user)
