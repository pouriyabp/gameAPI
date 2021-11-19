from .models import SignUp
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import login , authenticate

# Create your views here.


class AuthAPI(APIView):
    def get(self, request, format=None):
        try:
            enteredUname = request.GET['user']
            enteredToken = request.GET['token']
            uname = SignUp.objects.get(Username=enteredUname)
            #token = Token.objects.create(user=enteredToken)
            key = SignUp.objects.get(TokenPublic=enteredToken)
            user = authenticate(username=uname, password=key)
            # login(request, user)
            if user is not None:
                return Response({'User': uname}, status=status.HTTP_200_OK)
            else:
                return Response({'Authentication Failed!'},
                            status=status.HTTP_502_BAD_GATEWAY)

        except SignUp.DoesNotExist:
            return Response({'status': f"User with this Username not found!"},
                            status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({'status': f"Error happend!--->{e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
