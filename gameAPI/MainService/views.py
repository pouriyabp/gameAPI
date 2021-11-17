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


class NGamesBasedPlatformAPI(APIView):
    def get(self, request):
        try:
            from django.db.models import Q
            ######################################################################################

            # authenticate user code

            ######################################################################################
            number_of_games = request.GET['number']
            games_platform = request.GET['platform']
            games = GameSales.objects.filter(Q(Platform__icontains=games_platform)).order_by('Rank')[
                    :int(number_of_games)]
            serialized_data = serializers.SingleGameSerializer(games, many=True)
            data = serialized_data.data
            if len(data) == 0:
                return Response({'status': f"Games for platform= '{games_platform}' not found!"},
                                status=status.HTTP_404_NOT_FOUND)
            return Response({'data': data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'status': f"Error happend!--->{e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class NGamesBasedYearAPI(APIView):
    def get(self, request):
        try:
            from django.db.models import Q
            ######################################################################################

            # authenticate user code

            ######################################################################################
            number_of_games = request.GET['number']
            games_year = request.GET['year']
            games = GameSales.objects.filter(Q(Year__icontains=games_year)).order_by('Rank')[
                    :int(number_of_games)]
            serialized_data = serializers.SingleGameSerializer(games, many=True)
            data = serialized_data.data
            if len(data) == 0:
                return Response({'status': f"Games in year= '{games_year}' not found!"},
                                status=status.HTTP_404_NOT_FOUND)
            return Response({'data': data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'status': f"Error happend!--->{e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class NGamesBasedGenreAPI(APIView):
    def get(self, request):
        try:
            from django.db.models import Q
            ######################################################################################

            # authenticate user code

            ######################################################################################
            number_of_games = request.GET['number']
            games_genre = request.GET['genre']
            games = GameSales.objects.filter(Q(Genre__icontains=games_genre)).order_by('Rank')[
                    :int(number_of_games)]
            serialized_data = serializers.SingleGameSerializer(games, many=True)
            data = serialized_data.data
            if len(data) == 0:
                return Response({'status': f"Games with genre= '{games_genre}' not found!"},
                                status=status.HTTP_404_NOT_FOUND)
            return Response({'data': data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'status': f"Error happend!--->{e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class FiveTopGamesAPI(APIView):
    def get(self, request):
        try:
            from django.db.models import Q
            ######################################################################################

            # authenticate user code

            ######################################################################################
            games_platform = request.GET['platform']
            games_year = request.GET['year']
            games_genre = request.GET['genre']
            games = GameSales.objects.filter(Q(Genre__icontains=games_genre, Year__icontains=games_year,
                                               Platform__icontains=games_platform)).order_by('Rank')[:5]
            serialized_data = serializers.SingleGameSerializer(games, many=True)
            data = serialized_data.data
            if len(data) == 0:
                return Response({
                    'status': f"Games with genre= '{games_genre}' and platform= {games_platform} "
                              f"and year= {games_year} not found!"}, status=status.HTTP_404_NOT_FOUND)
            return Response({'data': data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'status': f"Error happend!--->{e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GamesEUgtNAAPI(APIView):
    def get(self, request):
        try:
            from django.db.models import Q
            from django.db.models import F
            ######################################################################################

            # authenticate user code

            ######################################################################################
            games = GameSales.objects.filter(Q(EU_Sales__gt=F('NA_Sales'))).order_by('Rank')[:20]
            serialized_data = serializers.SingleGameSerializer(games, many=True)
            data = serialized_data.data
            if len(data) == 0:
                return Response({'status': f"No games found that EU sales is greater than NA sales."})
            return Response({'data': data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'status': f"Error happend!--->{e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
