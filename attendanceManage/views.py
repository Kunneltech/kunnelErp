from .models import attendanceManage
from rest_framework.views import APIView
from .serializers import attendanceSerializer
from rest_framework.response import Response

class attendanceViews(APIView):

    def get(self,request):
        data = attendanceManage.objects.all()
        serialized = attendanceSerializer(data,many=True)
        return Response(serialized.data)

    def post(self,request):
        recivedata = recivedata.data
        serialized = attendanceSerializer(data=recivedata)
        if serialized.is_valid():
            attendaceRes = serialized.save()
            print("print attence response",attendaceRes)
            attendanceRes = {"status","attendace added suceefully"}
            return Response(attendaceRes)