from .models import shiftInfo
from rest_framework import serializers

class shiftInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = shiftInfo
        fields = '__all__'
