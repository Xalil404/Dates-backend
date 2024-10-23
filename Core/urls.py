"""
URL configuration for Core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from .views import handler404
from django.contrib import admin
from django.urls import path, include

# These imports for swagger api documentation 
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# Swagger UI: http://127.0.0.1:8000/swagger/
# ReDoc UI: http://127.0.0.1:8000/redoc/

schema_view = get_schema_view(
    openapi.Info(
        title="Your Project API",
        default_version="v1",
        description="API documentation for the project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourdomain.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('', include('home.urls')),
    path('api/', include('BirthdaysAPI.urls')),
    path('api/', include('AnniversariesAPI.urls')),
    path('api/', include('HolidaysAPI.urls')),
    path('api/', include('profileAPI.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/auth/', include('dj_rest_auth.urls')),  # Login, Logout, Password Change, etc.
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),  # Sign-up
]
handler404 = 'Core.views.handler404'



