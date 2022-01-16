from rest_framework import serializers
from .models import CodeModel


class CodeSerializer(serializers.modelSerializer):
    class Meta:
        model = CodeModel
        fields = ('uuid_field','created_at',)