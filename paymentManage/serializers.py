from .models import paymentInfo
from rest_framework import serializers

class paymentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = paymentInfo
        fields = '__all__'
