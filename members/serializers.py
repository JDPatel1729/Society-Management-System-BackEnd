from rest_framework.serializers import ModelSerializer

from .models import Members

class MemberSerializer(ModelSerializer);
	class Meta;
		model = Members
		fields = "__all__" 