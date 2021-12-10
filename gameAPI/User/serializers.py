from rest_framework import serializers

class SingleUserSerializer(serializers.Serializer):
    Username = serializers.CharField(required=True, allow_blank=False, max_length=128)
    TokenPublic = serializers.CharField(required=True, allow_blank=False, max_length=1024)