from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import client, punct_lucru, calendar_rezervare, judet, localitate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.
@api_view(['GET'])
def get_clienti(request):
    if request.method == 'GET':
        clienti = client.Client.objects.all()
        serializer = client.ClientSerializer(clienti, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def register_client(request):
    try:
        client.Client.register_client(request.data)
        data = {"success": "Inregistrare facuta cu succes. Am trimis un cod de activare la adresa de email specificata."}
        return Response(data=data, status=status.HTTP_201_CREATED)
    except Exception as e:
        error_msg = str(e).split(' ', 1)[1].split('\n', 1)[0]
        data = {"error": error_msg}
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    try:
        client_email = client.Client.login(request.data)
        data = {"success": "Login efectuat cu succes.",
                "client_email": client_email}
        return Response(data=data, status=status.HTTP_200_OK)
    except Exception as e:
        error_msg = str(e).split(' ', 1)[1].split('\n', 1)[0]
        print(e)
        data = {"error": error_msg}
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_puncte_lucru(request, client_token):
    if client_token is None or len(client_token) < 32:
        return Response(data={"error": "Invalid client token"}, status=status.HTTP_400_BAD_REQUEST)
    if client.Client.check_token(client_token) == 'N':
        return Response(data={"error": "Invalid client token"}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        puncte_lucru = punct_lucru.PunctLucru.objects.all()
        serializer = punct_lucru.PunctLucruSerializer(puncte_lucru, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def inregistrare_rezervare(request, client_token):
    if client_token is None or len(client_token) < 32:
        return Response(data={"error": "Invalid client token"}, status=status.HTTP_400_BAD_REQUEST)
    if client.Client.check_token(client_token) == 'N':
        return Response(data={"error": "Invalid client token"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        calendar_rezervare.CalendarRezervare.inregistrare_rezervare(request.data)
        data = {"success": "Cererea de rezervare a fost trimisa."}
        return Response(data=data, status=status.HTTP_200_OK)
    except Exception as e:
        error_msg = str(e).split(' ', 1)[1].split('\n', 1)[0]
        print(e)
        data = {"error": error_msg}
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def validare_rezervare(request):
    # if client_token is None or len(client_token) < 32:
    #     return Response(data={"error": "Invalid client token"}, status=status.HTTP_400_BAD_REQUEST)
    # if client.Client.check_token(client_token) == 'N':
    #     return Response(data={"error": "Invalid client token"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        calendar_rezervare.CalendarRezervare.validare_rezervare(request.data)
        data = {"success": "Cerere validata cu succes, rezervarea a fost creata."}
        return Response(data=data, status=status.HTTP_200_OK)
    except Exception as e:
        error_msg = str(e).split(' ', 1)[1].split('\n', 1)[0]
        print(e)
        data = {"error": error_msg}
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_judete(request):
    if request.method == 'GET':
        judete = judet.Judet.get_judete()
        return Response(judete)


@api_view(['POST'])
def get_localitati(request):
    try:
        localitati = localitate.Localitate.get_localitati(request.data)
        return Response(localitati, status=status.HTTP_200_OK)
    except Exception as e:
        error_msg = str(e).split(' ', 1)[1].split('\n', 1)[0]
        print(e)
        data = {"error": error_msg}
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

