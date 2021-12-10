from rest_framework import response
from .models import GameSales
from User.models import SignUp
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
from . import serializers


# Create your views here.

class GamesBasedRankAPI(APIView):
    def get(self, request, format=None):
        try:
            ######################################################################################
            try:
                enteredUname = request.GET['user']
                enteredToken = request.GET['token']

                # uname = SignUp.objects.using('users').get(Username=enteredUname)
                # uname = SignUp.objects.values('Username')
                # # keyPair = RSA.generate(2048)
                # pubKey = keyPair.publickey()
                # # print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
                # TokenPublic = pubKey.exportKey()
                # print(uname.TokenPublic.decode('ascii'))
                # print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
                # privKeyPEM = keyPair.exportKey()
                # print(privKeyPEM.decode('ascii'))

                for user in SignUp.objects.all():

                    if enteredUname == user.Username:

                        if enteredToken == user.TokenPublic:

                            game_rank = request.GET['rank']
                            game = GameSales.objects.get(Rank=int(game_rank))
                            serialized_data = serializers.SingleGameSerializer(game)
                            data = serialized_data.data
                            return Response({'data': data}, status=status.HTTP_200_OK)

                        else:
                            return Response({'Wrong Token. Please Enter Right Token!'}, status=status.HTTP_404_NOT_FOUND)
                    
                    else:
                        return Response({'User Not Found. Please Enter Right Username!'}, status=status.HTTP_400_BAD_REQUEST)

            except SignUp.DoesNotExist:
                return Response({'status': f"User not found in Database!"},
                            status=status.HTTP_404_NOT_FOUND)

            except Exception as e:
                return Response({'status': f"Error happend!--->{e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            ######################################################################################

            

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

            try:
                enteredUname = request.GET['user']
                enteredToken = request.GET['token']

                for user in SignUp.objects.all():

                    if enteredUname == user.Username:

                        if enteredToken == user.TokenPublic:

                            game_name = request.GET['name']
                            games = GameSales.objects.filter(Q(Name__icontains=game_name))
                            serialized_data = serializers.SingleGameSerializer(
                                games, many=True)
                            data = serialized_data.data
                            if len(data) == 0:
                                return Response({'status': f"Game with name= '{game_name}' not found!"},
                                                    status=status.HTTP_404_NOT_FOUND)
                            return Response({'data': data}, status=status.HTTP_200_OK)

                        else:
                            return Response({'Wrong Token. Please Enter Right Token!'}, status=status.HTTP_404_NOT_FOUND)
                    
                    else:
                        return Response({'User Not Found. Please Enter Right Username!'}, status=status.HTTP_400_BAD_REQUEST)

            except SignUp.DoesNotExist:
                return Response({'status': f"User not found in Database!"},
                            status=status.HTTP_404_NOT_FOUND)

            except Exception as e:
                return Response({'status': f"Error happend!--->{e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            ######################################################################################
            

        except Exception as e:
            return Response({'status': f"Error happend!--->{e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
