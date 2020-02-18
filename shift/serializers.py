from .models import shift
from rest_framework import serializers

class shiftInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = shift
        fields = '__all__'
        
