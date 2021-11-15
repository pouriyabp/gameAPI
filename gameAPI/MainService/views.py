from django.http import response
from django.shortcuts import render
from .models import GameSales
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
# Create your views here.

class GamesBasedRankAPI(APIView):
    def get(self, request, format= None):
        try:
            ######################################################################################


            # authenticate user code


            ######################################################################################
            game_rank = request.GET['rank']
            game = GameSales.objects.filter(Rank=int(game_rank))
            serialized_data = serializers.SingleGameSerializer(game, many=True)
            data = serialized_data.data
  
            return Response({'data': data}, status= status.HTTP_200_OK)

        except:
            pass