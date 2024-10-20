from rest_framework import serializers
from .models import Anniversary

class AnniversarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Anniversary
        fields = '__all__'
