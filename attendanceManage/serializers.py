from .models import attendanceManage,labourWorkTime
from rest_framework import serializers

class attendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = attendanceManage
        fields = '__all__'



class labourerworkTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = labourWorkTime
        fields = '__all__'

# class checkingSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = labourWorkTime
#         fields =
