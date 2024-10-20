from django.urls import path
from .views import AnniversaryListCreateView, AnniversaryDetailView

urlpatterns = [
    # List all anniversaries and create a new one
    path('anniversaries/', AnniversaryListCreateView.as_view(), name='anniversary-list-create'),
    
    # Retrieve, update, or delete a specific anniversary by ID
    path('anniversaries/<int:pk>/', AnniversaryDetailView.as_view(), name='anniversary-detail'),
]
