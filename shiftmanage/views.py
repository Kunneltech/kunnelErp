from rest_framework.response import Response
from .models import shiftInfo
from .serializers import shiftInfoSerializer
from rest_framework.views import APIView



class shiftView(APIView):
    def get(self,request):
        dbdata = shiftInfo.objects.all()
        serilized = shiftInfoSerializer(dbdata,many=True)      
        return Response(serilized.data)        


    def post(self,request):
        recivedata = request.data
        serialized = shiftInfoSerializer(data=recivedata)
        if serialized.is_valid():
            serialized.save()
            response = {"satus":"shift added sucessfully created sucessfully"}
            return Response(response)  