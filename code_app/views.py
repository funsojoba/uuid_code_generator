import uuid
from datetime import datetime
from rest_framework import status, response, views

from .models import CodeModel
from .serializers import CodeSerializer


def generate_uuid():
    return CodeModel.objects.create(uuid_field=datetime.now())


class CodeView(views.APIView):
    def get_code(self, request):
        generate_uuid()
        
        queryset = CodeModel.objects.all()
        serializer = CodeSerializer(queryset, many=True)
        serializer.is_valid()
        return response.Response({"data":serializer.data}, status=status.HTTP_200)