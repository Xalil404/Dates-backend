from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import UserProfile
from .serializers import UserProfileSerializer

# yourapp/views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from allauth.account.utils import perform_login
from allauth.account.views import LoginView
from .serializers import LoginSerializer  # Create this serializer


class UserProfileDetailView(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Customize how the user profile is retrieved
        return self.request.user.profile 

class CustomLoginView(LoginView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                perform_login(request, user)
                return Response({"success": "User logged in successfully!"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


