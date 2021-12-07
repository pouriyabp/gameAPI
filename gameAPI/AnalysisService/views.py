from MainService.models import GameSales
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from MainService import serializers
import matplotlib.pyplot as plt
import numpy as np


# Create your views here.

class CompareTwoGamesAPI(APIView):
    def get(self, request):
        try:
            ######################################################################################

            # authenticate user code

            ######################################################################################

            first_game = request.GET['game1']
            second_game = request.GET['game2']
            # use exact name ---> icontains for contain name.
            first_game_object = GameSales.objects.filter(Name__iexact=first_game)
            second_game_object = GameSales.objects.filter(Name__iexact=second_game)
            serialized_data_first_game = serializers.SingleGameSerializer(first_game_object, many=True)
            serialized_data_second_game = serializers.SingleGameSerializer(second_game_object, many=True)
            first_game_data = serialized_data_first_game.data
            second_game_data = serialized_data_second_game.data

            # analysis data:
            first_game_NA_sales = 0.0
            first_game_EU_sales = 0.0
            first_game_JP_sales = 0.0
            first_game_other_sales = 0.0
            first_game_global_sales = 0.0
            second_game_NA_sales = 0.0
            second_game_EU_sales = 0.0
            second_game_JP_sales = 0.0
            second_game_other_sales = 0.0
            second_game_global_sales = 0.0
            for game in first_game_data:
                first_game_NA_sales += game['NA_Sales']
                first_game_EU_sales += game['EU_Sales']
                first_game_JP_sales += game['JP_Sales']
                first_game_other_sales += game['Other_Sales']
                first_game_global_sales += game['Global_Sales']

            for game in second_game_data:
                second_game_NA_sales += game['NA_Sales']
                second_game_EU_sales += game['EU_Sales']
                second_game_JP_sales += game['JP_Sales']
                second_game_other_sales += game['Other_Sales']
                second_game_global_sales += game['Global_Sales']

            first_game_sales = {
                'NA_sales': first_game_NA_sales,
                'EU_Sales': first_game_EU_sales,
                'JP_Sales': first_game_JP_sales,
                'Other_Sales': first_game_other_sales,
                'Global_Sales': first_game_global_sales,
            }
            second_game_sales = {
                'NA_sales': second_game_NA_sales,
                'EU_Sales': second_game_EU_sales,
                'JP_Sales': second_game_JP_sales,
                'Other_Sales': second_game_other_sales,
                'Global_Sales': second_game_global_sales,
            }
            # the ugly version of bar chars ---> like project
            # x = np.array(
            #     ['NA_sales1', 'EU_Sales1', 'JP_Sales1', 'Other_Sales1', 'Global_Sales1', 'NA_sales2', 'EU_Sales2',
            #      'JP_Sales2', 'Other_Sales2', 'Global_Sales2'])
            # y = np.array([first_game_NA_sales, first_game_EU_sales, first_game_JP_sales, first_game_other_sales,
            #               first_game_global_sales, second_game_NA_sales, second_game_EU_sales, second_game_JP_sales,
            #               second_game_other_sales, second_game_global_sales])
            # x_pos = [0, 1, 2, 3, 4, 9, 10, 11, 12, 13]
            # plt.bar(x_pos, y, width=0.25,
            #         color=['black', 'red', 'green', 'blue', 'cyan', 'black', 'red', 'green', 'blue', 'cyan'])
            # plt.xticks(x_pos)

            first_game_data = [first_game_NA_sales, first_game_EU_sales, first_game_JP_sales, first_game_other_sales,
                               first_game_global_sales, ]
            second_game_data = [second_game_NA_sales, second_game_EU_sales, second_game_JP_sales,
                                second_game_other_sales, second_game_global_sales]
            n = 5
            r = np.arange(n)
            width = 0.25
            plt.bar(r, first_game_data, color='b', width=width, edgecolor='black', label=f'{first_game}')
            plt.bar(r + width, second_game_data, color='g', width=width, edgecolor='black', label=f'{second_game}')
            plt.title(f"{first_game} VS {second_game} ")
            plt.xticks(r + width / 2, ['NA_sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales'])
            plt.legend()
            plt.show()
            base64_jpgData = 0

            # convert image to base64 format for api
            # import base64
            # import io
            # my_stringIObytes = io.BytesIO()
            # plt.savefig(my_stringIObytes, format='jpg')
            # my_stringIObytes.seek(0)
            # base64_jpgData = base64.b64encode(my_stringIObytes.read())
            return Response({'data1': first_game_sales, 'data2': second_game_sales, 'chart': base64_jpgData},
                            status=status.HTTP_200_OK)

        except GameSales.DoesNotExist:
            return Response({'status': f"Game with not found!"},
                            status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'status': f"Error happend!--->{e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class YearsSalesAPI(APIView):
    def get(self, request):
        try:
            ######################################################################################

            # authenticate user code

            ######################################################################################

            start_year = int(request.GET['start'])
            end_year = int(request.GET['end'])
            year_dict = {}
            for year in range(start_year, end_year+1):
                games = GameSales.objects.filter(Year__iexact=str(year))
                serialized_data_first_game= serializers.SingleGameSerializer(games, many=True)
                games_data = serialized_data_first_game.data
                temp = 0 # for save global sales of one year
                for game in games_data:
                    temp += game['Global_Sales']
                year_dict[str(year)] = temp

            plt.bar(range(len(year_dict)), list(year_dict.values()), align='center')
            plt.xticks(range(len(year_dict)), list(year_dict.keys()))
            plt.title(f"Global sales from {start_year} to {end_year} ")
            plt.show()

            return Response({'data':year_dict}, status=status.HTTP_200_OK)

        except GameSales.DoesNotExist:
            return Response({'status': f"Game with not found!"},
                            status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'status': f"Error happend!--->{e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
