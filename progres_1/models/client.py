from django.db import models
from progres_1.handled_cursor import HandledCursor
from django.core.mail import send_mail
from rest_framework import serializers
from progres_1.models import localitate


class Client(models.Model):
    id = models.IntegerField(primary_key=True)
    nume = models.CharField(max_length=64, blank=True, null=True)
    prenume = models.CharField(max_length=64, blank=True, null=True)
    email = models.CharField(unique=True, max_length=64, blank=True, null=True)
    username = models.CharField(unique=True, max_length=32, blank=True, null=True)
    telefon = models.CharField(max_length=64, blank=True, null=True)
    localitate = models.ForeignKey(localitate.Localitate, models.DO_NOTHING)
    rata_prezenta = models.IntegerField()
    parola = models.CharField(max_length=64)
    cont_valid = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'clienti'

    @staticmethod
    def register_client(data):
        handled_cursor = HandledCursor()
        parameters = []

        for param in data:
            parameters.append(data[param])
        handled_cursor.callproc("client_management.register_client", parameters)

        register_token = handled_cursor.callfunc("client_management.get_cod_inregistrare", str, [data["email"]])

        subject = "Activare cont PROGRES"
        body = "Buna, " + data["prenume"] + ".\nFoloseste acest cod la activarea contului tau: " + register_token + "\nAi grija, expira in 3 ore.\n\nGanduri bune,\nEchipa Progres"
        sender = "progres@progres_app.com"
        recipients = [data["email"]]
        send_mail(subject, body, sender, recipients, fail_silently=False)

    @staticmethod
    def add_recenzie(data):
        handled_cursor = HandledCursor()
        parameters = []

        for param in data:
            parameters.append(data[param])
        handled_cursor.callproc("client_management.add_recenzie", parameters)

    @staticmethod
    def generare_cod_inregistrare(data):
        handled_cursor = HandledCursor()
        parameters = []

        for param in data:
            parameters.append(data[param])
        handled_cursor.callproc("client_management.generare_cod_inregistrare", parameters)

    @staticmethod
    def validare_cont_client(data):
        handled_cursor = HandledCursor()
        parameters = []

        for param in data:
            parameters.append(data[param])
        handled_cursor.callproc("client_management.validare_cont_client", parameters)

    @staticmethod
    def get_cod_inregistrare(data):
        handled_cursor = HandledCursor()
        parameters = []

        for param in data:
            parameters.append(data[param])
        return_val = handled_cursor.callfunc("client_management.get_cod_inregistrare", str, parameters)
        return return_val

    @staticmethod
    def login(data):
        handled_cursor = HandledCursor()
        parameters = []

        for param in data:
            parameters.append(data[param])
        client_email = handled_cursor.callfunc("client_management.login", str, parameters)
        return client_email

    @staticmethod
    def create_client_token(data):
        handled_cursor = HandledCursor()
        parameters = []

        for param in data:
            parameters.append(data[param])
        handled_cursor.callproc("client_management.create_client_token", parameters)

    @staticmethod
    def get_client_tokens(data):
        handled_cursor = HandledCursor()
        parameters = []

        for param in data:
            parameters.append(data[param])
        tokens = handled_cursor.callfunc("client_management.get_client_tokens", str, parameters)
        return tokens

    @staticmethod
    def check_token(token):
        handled_cursor = HandledCursor()
        parameters = []
        parameters.append(token)
        result = handled_cursor.callfunc("client_management.check_token", str, parameters)
        return result


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['nume', 'prenume', 'email', 'localitate']