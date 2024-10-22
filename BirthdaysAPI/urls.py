from django.urls import path
from .views import BirthdayListCreateView, BirthdayRetrieveUpdateDestroyView  # Import existing views

urlpatterns = [
    path('birthdays/', BirthdayListCreateView.as_view(), name='birthday-list-create'),
    path('birthdays/<int:pk>/', BirthdayRetrieveUpdateDestroyView.as_view(), name='birthday-detail'),
]
