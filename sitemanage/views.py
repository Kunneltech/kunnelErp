
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SiteManageSerializer, SiteManageCreateSerializer
from .models import SiteManage

from rest_framework import viewsets
from django.shortcuts import get_object_or_404

class SiteAPIView(viewsets.ViewSet):

	def list(self, request):
		data = SiteManage.objects.all()
		serializer = SiteManageSerializer(data, many=True)
		return Response(serializer.data)


	def post(self, request, format=None):
		serializer = SiteManageCreateSerializer(data=request.data)
		print(request.data)
		if serializer.is_valid():
			serializer.save()
			data = serializer.data
			api = '/sitemanage/sites/{}/'.format(data.get('id'))
			return Response({"satus":"created","data":serializer.data,"url":api})
		return Response({"satus":"failed"})

	def retrive(self, request, pk=None):
	    queryset = SiteManage.objects.all()
	    data = get_object_or_404(queryset, pk=pk)
	    serializer = SiteManageSerializer(data)
	    return Response(serializer.data)




from rest_framework.decorators import api_view, permission_classes, renderer_classes, schema
from django.views.decorators.csrf import csrf_exempt
from labourer.models import LabourerManage

 
@api_view(["POST"])
def addLabourerToSiteAPIView(request):
	try:
		site_id = request.data.get("site_id")
		labourer = request.data.get("labourer")
		site = get_object_or_404(SiteManage, site_id=site_id)
		for i in labourer:
			lab = get_object_or_404(LabourerManage, labourerid=i)
			lab.site_id = site_id
			lab.save()
		return Response({"satus":True,"message":"labours addedd"})
	except:
		return Response({"satus":False,"message":"internal error"})        