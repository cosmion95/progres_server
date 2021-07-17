from progres_1.models import client, punct_lucru, calendar_rezervare
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import time

# VIEW-URI FOLOSITE LA REGISTER SI VALIDARE CONT PRIN 2FA
@api_view(['POST'])
def register_client(request):
    try:
        data = client.Client.register_client(request.data)
        return Response(data=data, status=status.HTTP_201_CREATED)
    except Exception as e:
        print(e)
        error_msg = str(e).split(' ', 1)[1].split('\n', 1)[0]
        data = {"error": error_msg}
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def generare_cod_inregistrare(request, token):
    if token is None or len(token) < 32 or client.Client.check_token(token, 'N', 'N', None) == 'N':
        return Response(data={"error": "Nu aveti autorizare pentru a accesa continutul"},
                        status=status.HTTP_400_BAD_REQUEST)
    try:
        client.Client.generare_cod_inregistrare(request.data)
        data = {"success": "Cod generat cu succes."}
        return Response(data=data, status=status.HTTP_201_CREATED)
    except Exception as e:
        error_msg = str(e).split(' ', 1)[1].split('\n', 1)[0]
        data = {"error": error_msg}
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def validare_cont_client(request, token):
    if token is None or len(token) < 32 or client.Client.check_token(token, 'N', 'N', None) == 'N':
        return Response(data={"error": "Nu aveti autorizare pentru a accesa continutul"},
                        status=status.HTTP_400_BAD_REQUEST)
    try:
        client.Client.validare_cont_client(request.data)
        data = {"success": "Cont activat cu succes."}
        return Response(data=data, status=status.HTTP_200_OK)
    except Exception as e:
        error_msg = str(e).split(' ', 1)[1].split('\n', 1)[0]
        data = {"error": error_msg}
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

# VIEW-URI FOLOSITE LA LOGIN SI VALIDARE LOGIN PRIN 2FA
@api_view(['POST'])
def login(request):
    try:
        client_token = client.Client.login(request.data)
        return Response(client_token, status=status.HTTP_200_OK)
    except Exception as e:
        error_msg = str(e).split(' ', 1)[1].split('\n', 1)[0]
        print(e)
        data = {"error": error_msg}
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def generare_cod_login(request, token):
    if token is None or len(token) < 32 or client.Client.check_token(token, 'D', 'N', None) == 'N':
        return Response(data={"error": "Nu aveti autorizare pentru a accesa continutul"},
                        status=status.HTTP_400_BAD_REQUEST)
    try:
        client.Client.generare_cod_login(request.data)
        data = {"success": "Cod generat cu succes."}
        return Response(data=data, status=status.HTTP_201_CREATED)
    except Exception as e:
        error_msg = str(e).split(' ', 1)[1].split('\n', 1)[0]
        data = {"error": error_msg}
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def validare_login(request, token):
    if token is None or len(token) < 32 or client.Client.check_token(token, 'D', 'N', None) == 'N':
        return Response(data={"error": "Nu aveti autorizare pentru a accesa continutul"},
                        status=status.HTTP_400_BAD_REQUEST)
    try:
        client.Client.validare_login(request.data)
        data = {"success": "Login efectuat cu succes."}
        return Response(data=data, status=status.HTTP_200_OK)
    except Exception as e:
        error_msg = str(e).split(' ', 1)[1].split('\n', 1)[0]
        data = {"error": error_msg}
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def inregistrare_rezervare(request, token):
    time.sleep(1)
    if token is None or len(token) < 32 or client.Client.check_token(token, 'D', 'D', request.data['client_id']) == 'N':
        return Response(data={"error": "Nu aveti autorizare pentru a accesa continutul"},
                        status=status.HTTP_400_BAD_REQUEST)
    try:
        calendar_rezervare.CalendarRezervare.inregistrare_rezervare(request.data)
        data = {"success": "Cererea de rezervare a fost creata cu succes."}
        return Response(data=data, status=status.HTTP_200_OK)
    except Exception as e:
        error_msg = str(e).split(' ', 1)[1].split('\n', 1)[0]
        print(e)
        data = {"error": error_msg}
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def validare_rezervare(request, token):
    if token is None or len(token) < 32 or client.Client.check_token(token, 'D', 'D', None) == 'N':
        return Response(data={"error": "Nu aveti autorizare pentru a accesa continutul"},
                        status=status.HTTP_400_BAD_REQUEST)
    try:
        calendar_rezervare.CalendarRezervare.validare_rezervare(request.data)
        data = {"success": "Cerere validata cu succes, rezervarea a fost creata."}
        return Response(data=data, status=status.HTTP_200_OK)
    except Exception as e:
        error_msg = str(e).split(' ', 1)[1].split('\n', 1)[0]
        print(e)
        data = {"error": error_msg}
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def get_client_from_email(request, token):
    if token is None or len(token) < 32 or client.Client.check_token(token, 'D', 'D', None) == 'N':
        return Response(data={"error": "Nu aveti autorizare pentru a accesa continutul"},
                        status=status.HTTP_400_BAD_REQUEST)
    try:
        result = client.Client.get_client_from_email(request.data)
        return Response(result, status=status.HTTP_200_OK)
    except Exception as e:
        error_msg = str(e).split(' ', 1)[1].split('\n', 1)[0]
        print(e)
        data = {"error": error_msg}
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def get_detalii_rezervare(request, token):
    if token is None or len(token) < 32 or client.Client.check_token(token, 'D', 'D', None) == 'N':
        return Response(data={"error": "Nu aveti autorizare pentru a accesa continutul"},
                        status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'POST':
        try:
            detalii = calendar_rezervare.CalendarRezervare.get_detalii_rezervare(request.data)
            return Response(detalii)
        except Exception as e:
            error_msg = str(e).split(' ', 1)[1].split('\n', 1)[0]
            print(e)
            data = {"error": error_msg}
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def anulare_rezervare(request, token):
    time.sleep(1)
    if token is None or len(token) < 32 or client.Client.check_token(token, 'D', 'D', request.data['client_id']) == 'N':
        return Response(data={"error": "Nu aveti autorizare pentru a accesa continutul"},
                        status=status.HTTP_400_BAD_REQUEST)
    try:
        calendar_rezervare.CalendarRezervare.anulare_client(request.data)
        data = {"success": "Rezervare anulata cu succes."}
        return Response(data=data, status=status.HTTP_200_OK)
    except Exception as e:
        error_msg = str(e).split(' ', 1)[1].split('\n', 1)[0]
        print(e)
        data = {"error": error_msg}
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def get_salt(request):
    if request.method == 'POST':
        try:
            program = client.Client.get_salt(request.data)
            return Response(program)
        except Exception as e:
            error_msg = str(e).split(' ', 1)[1].split('\n', 1)[0]
            print(e)
            data = {"error": error_msg}
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


