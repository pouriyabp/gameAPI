from typing_extensions import Required
from rest_framework import serializers

class SingleGameSerializer(serializers.Serializer):
    Name = serializers.CharField(required=True, allow_blank=False, max_length=128)
