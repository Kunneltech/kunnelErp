from .models import labourerclass
from rest_framework import serializers

class labourerclassSerializer(serializers.ModelSerializer):
    class Meta:
        model = labourerclass
        fields = '__all__'
