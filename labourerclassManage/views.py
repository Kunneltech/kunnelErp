from rest_framework.response import Response
from rest_framework.views import APIView
from .models import labourerclass
from .serializers import labourerclassSerializer



class labourerclassView(APIView):
    def get(self,request):
        dbdata = labourerclass.objects.all()
        serilized = labourerclassSerializer(dbdata,many=True)
        return Response(serilized.data)


    def post(self,request):
        recivedata = request.data
        serialized = labourerclassSerializer(data=recivedata)
        if serialized.is_valid():
            serialized.save()
            response = {"satus":"labourerclass added sucessfully created sucessfully"}
            return Response(response)