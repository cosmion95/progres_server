from progres_1.models import punct_lucru, client
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def get_puncte_lucru(request, token):
    if token is None or len(token) < 32 or client.Client.check_token(token, 'D', 'D') == 'N':
        return Response(data={"error": "Nu aveti autorizare pentru a viziona continutul"},
                        status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'POST':
        puncte_lucru = punct_lucru.PunctLucru.get_puncte_lucru(request.data)
        if puncte_lucru == "]":
            return Response(data={"error": "Nu am gasit puncte de lucru."},
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(puncte_lucru)

@api_view(['POST'])
def get_program_punct(request, token):
    if token is None or len(token) < 32 or client.Client.check_token(token, 'D', 'D') == 'N':
        return Response(data={"error": "Nu aveti autorizare pentru a viziona continutul"},
                        status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'POST':
        try:
            program = punct_lucru.PunctLucru.get_program_punct(request.data)
            return Response(program)
        except Exception as e:
            error_msg = str(e).split(' ', 1)[1].split('\n', 1)[0]
            print(e)
            data = {"error": error_msg}
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def get_urmatoarea_zi_lucratoare(request, token):
    if token is None or len(token) < 32 or client.Client.check_token(token, 'D', 'D') == 'N':
        return Response(data={"error": "Nu aveti autorizare pentru a viziona continutul"},
                        status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'POST':
        try:
            program = punct_lucru.PunctLucru.get_urmatoarea_zi_lucratoare(request.data)
            return Response(program)
        except Exception as e:
            error_msg = str(e).split(' ', 1)[1].split('\n', 1)[0]
            print(e)
            data = {"error": error_msg}
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def get_procent_ocupare(request, token):
    if token is None or len(token) < 32 or client.Client.check_token(token, 'D', 'D') == 'N':
        return Response(data={"error": "Nu aveti autorizare pentru a viziona continutul"},
                        status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'POST':
        try:
            program = punct_lucru.PunctLucru.get_procent_ocupare(request.data)
            return Response(program)
        except Exception as e:
            error_msg = str(e).split(' ', 1)[1].split('\n', 1)[0]
            print(e)
            data = {"error": error_msg}
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def get_program_neeligibil(request, token):
    if token is None or len(token) < 32 or client.Client.check_token(token, 'D', 'D') == 'N':
        return Response(data={"error": "Nu aveti autorizare pentru a viziona continutul"},
                        status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'POST':
        try:
            program = punct_lucru.PunctLucru.get_program_neeligibil(request.data)
            return Response(program)
        except Exception as e:
            error_msg = str(e).split(' ', 1)[1].split('\n', 1)[0]
            print(e)
            data = {"error": error_msg}
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def verificare_timp_ales(request, token):
    if token is None or len(token) < 32 or client.Client.check_token(token, 'D', 'D') == 'N':
        return Response(data={"error": "Nu aveti autorizare pentru a viziona continutul"},
                        status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'POST':
        try:
            program = punct_lucru.PunctLucru.verificare_timp_ales(request.data)
            return Response(program)
        except Exception as e:
            error_msg = str(e).split(' ', 1)[1].split('\n', 1)[0]
            print(e)
            data = {"error": error_msg}
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def get_tipuri_rezervare(request, token):
    if token is None or len(token) < 32 or client.Client.check_token(token, 'D', 'D') == 'N':
        return Response(data={"error": "Nu aveti autorizare pentru a viziona continutul"},
                        status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'POST':
        try:
            program = punct_lucru.PunctLucru.get_tipuri_rezervare(request.data)
            return Response(program)
        except Exception as e:
            error_msg = str(e).split(' ', 1)[1].split('\n', 1)[0]
            print(e)
            data = {"error": error_msg}
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)