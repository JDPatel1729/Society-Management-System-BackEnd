from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Service
from .serializers import ServiceSerializer

@api_view(["GET","POST","PUT","DELETE"])
def services(request):

	if request.method == "GET":
		service_list = Service.objects.filter(society_id=request.GET.get('society_id',None))
		serializer = ServiceSerializer(service_list, many=True)

		return Response(serializer.data)

	elif request.method == "POST":
		serializer = ServiceSerializer(data=request.data)
		
		if serializer.is_valid():
			serializer.save()

			return Response(serializer.data)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
	
	elif request.method == "PUT":
		service = Service.objects.get(id = request.GET.get('id',None))
		serializer = ServiceSerializer(instance=service,data=request.data)

		if serializer.is_valid():
			return Response(serializer.data)
		
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

	elif request.method == "DELETE":
		service = Service.objects.get(id = request.GET.get('id',None))
		service.delete()

		return Response(status = status.HTTP_204_NO_CONTENT)