from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import MemberSerializer
from .models import Members

@api_view(["GET",'POST','PUT','DELETE'])
def members(request):

	if request.method == 'GET':
		member_list = Members.objects.filter(society_id=request.GET.get('society_id',None))
		serializer = MemberSerializer(member_list, many=True)

		return Response(serializer.data)	

	elif request.method == "POST":
		serializer = MemberSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

	elif request.method == "PUT":
		member = Members.objects.get(id = request.GET.get('id',None))
		serializer = MemberSerializer(member,data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)

		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

	elif request.method == "DELETE":
		member = Members.objects.get(id = request.GET.get('id',None))
		member.delete()
		
		return Response(status = status.HTTP_204_NO_CONTENT)
