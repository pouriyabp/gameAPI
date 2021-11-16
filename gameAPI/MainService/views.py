from .models import GameSales
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers


# Create your views here.

class GamesBasedRankAPI(APIView):
    def get(self, request, format=None):
        try:
            ######################################################################################

            # authenticate user code

            ######################################################################################

            game_rank = request.GET['rank']
            game = GameSales.objects.get(Rank=int(game_rank))
            serialized_data = serializers.SingleGameSerializer(game)
            data = serialized_data.data
            return Response({'data': data}, status=status.HTTP_200_OK)

        except GameSales.DoesNotExist:
            return Response({'status': f"Game with rank= '{game_rank}' not found!"},
                            status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'status': f"Error happend!--->{e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GamesBasedNameAPI(APIView):
    def get(self, request):
        try:
            from django.db.models import Q
            ######################################################################################

            # authenticate user code

            ######################################################################################
            game_name = request.GET['name']
            games = GameSales.objects.filter(Q(Name__icontains=game_name))
            serialized_data = serializers.SingleGameSerializer(games, many=True)
            data = serialized_data.data
            if len(data) == 0:
                return Response({'status': f"Game with name= '{game_name}' not found!"},
                                status=status.HTTP_404_NOT_FOUND)
            return Response({'data': data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'status': f"Error happend!--->{e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
