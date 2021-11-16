from typing_extensions import Required
from rest_framework import serializers

class SingleGameSerializer(serializers.Serializer):
    Rank = serializers.IntegerField(required = True)
    Name = serializers.CharField(required=True, allow_blank=False, max_length=512)
    Platform = serializers.CharField(required=True, allow_blank=False, max_length=64)
    Year = serializers.CharField(required=True, allow_blank=False, max_length=64)
    Genre = serializers.CharField(required=True, allow_blank=False, max_length=128)
    Publisher = serializers.CharField(required=True, allow_blank=False, max_length=128)
    NA_Sales = serializers.FloatField(required = True)
    EU_Sales = serializers.FloatField(required = True)
    JP_Sales = serializers.FloatField(required = True)
    Other_Sales = serializers.FloatField(required = True)
    Global_Sales = serializers.FloatField(required = True)

