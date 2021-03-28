from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Ledger
from .serializers import LedgerSerializer

@api_view(['GET','POST','DELETE'])
def ledger(request):

	if request.method == "GET":
		transactions_list = Ledger.objects.filter(society_id=request.GET.get('society_id',None))
		serializer = LedgerSerializer(transactions_list,many = True)

		return Response(serializer.data)

	elif request.method == "POST":
		serializer = LedgerSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()

			return Response(serializer.data, status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_CONTENT)

	elif request.method == "DELETE":
		transaction = Ledger.objects.get(id = request.GET.get('id',None))
		transaction.delete()

		return Response(status=status.HTTP_204_NO_CONTENT)
		