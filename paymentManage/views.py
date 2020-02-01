from rest_framework.response import Response
from .models import paymentInfo
from rest_framework.views import APIView
from .serializers import paymentInfoSerializer



class paymentView(APIView):
    def get(self,request):
        dbdata = paymentInfo.objects.all()
        serilized = paymentInfoSerializer(dbdata,many=True)
        return Response(serilized.data)        


    def post(self,request):
        recivedata = request.data
        serialized = paymentInfoSerializer(data=recivedata)
        if serialized.is_valid():
            serialized.save()
            response = {"satus":"paymentinfo added sucessfully created sucessfully"}
            return Response(response)        