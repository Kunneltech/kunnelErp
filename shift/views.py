from rest_framework.response import Response
from .models import shift
from .serializers import shiftInfoSerializer
from rest_framework.views import APIView
from datetime import datetime



class shiftView(APIView):
    def totalTime(self,idval):
        times = shift.objects.filter(id=idval)
        serialdata = shiftInfoSerializer(times,many=True)
        print("........",(serialdata.data[0]['shiftstart']),(serialdata.data[0]['shiftend']))
        # print("........",type(datetime.strptime((serialdata.data[0]['shiftstart']),'%H::%M::%S').time()))
        # print('total times',totaltime)

    def get(self,request):
        dbdata = shift.objects.all()
        serilized = shiftInfoSerializer(dbdata,many=True)   
        ser1 = TotalWorkingtime(dbdata,many=True)   
        # print("seri1",ser1.data[0]['shiftstart'],ser1.data[0]['shiftend'])
        # print("serilizer",ser1.data)
        self.totalTime(2)
        return Response(serilized.data)    


    def post(self,request):
        recivedata = request.data
        serialized = shiftInfoSerializer(data=recivedata)
        if serialized.is_valid():
            serialized.save()
            response = {"satus":"shift added sucessfully created sucessfully"}
            return Response(response)  
