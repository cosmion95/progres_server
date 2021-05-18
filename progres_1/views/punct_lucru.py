from progres_1.models import punct_lucru, client
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import time


@api_view(['POST'])
def get_puncte_lucru(request, token):
    if token is None or len(token) < 32 or client.Client.check_token(token) == 'N':
        return Response(data={"error": "Nu aveti autorizare pentru a viziona continutul"},
                        status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'POST':
        puncte_lucru = punct_lucru.PunctLucru.get_puncte_lucru(request.data)
        print("gasit puncte")
        if puncte_lucru == "]":
            return Response(data={"error": "Nu exista puncte de lucru inregistrate la localitatea aleasa."},
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(puncte_lucru)