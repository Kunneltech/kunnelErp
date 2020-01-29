from .models import attendanceManage
from rest_framework import serializers

class attendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = attendanceManage
        fields = '__all__'

