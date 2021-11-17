from MainService.models import GameSales
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from MainService import serializers

# Create your views here.

class CompareTwoGamesAPI(APIView):
    def get(self, request):
        try:
            ######################################################################################

            # authenticate user code

            ######################################################################################

            first_game = request.GET['game1']
            second_game = request.GET['game2']
            first_game_object = GameSales.objects.filter(Name__icontains=first_game)
            second_game_object = GameSales.objects.filter(Name__icontains=second_game)

            serialized_data_first_game = serializers.SingleGameSerializer(first_game_object, many = True)
            serialized_data_second_game = serializers.SingleGameSerializer(second_game_object, many = True)
            first_game_data = serialized_data_first_game.data
            second_game_data = serialized_data_second_game.data
            return Response({'data1': first_game_data, 'data2' : second_game_data}, status=status.HTTP_200_OK)

        except GameSales.DoesNotExist:
            return Response({'status': f"Game with not found!"},
                            status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'status': f"Error happend!--->{e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

