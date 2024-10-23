from django.urls import path
from .views import UserProfileDetailView, CustomLoginView
from allauth.account.views import LoginView


urlpatterns = [
    path('profile/', UserProfileDetailView.as_view(), name='userprofile-detail'),
    path('api/auth/login/', LoginView.as_view(), name='login'),
    path('api/login/', CustomLoginView.as_view(), name='login'),
]
