from django.db import models
from progres_1.handled_cursor import HandledCursor
from django.core.mail import send_mail
from progres_1.models import localitate


class Client(models.Model):
    id = models.IntegerField(primary_key=True)
    nume = models.CharField(max_length=64, blank=True, null=True)
    prenume = models.CharField(max_length=64, blank=True, null=True)
    email = models.CharField(unique=True, max_length=64, blank=True, null=True)
    telefon = models.CharField(max_length=64, blank=True, null=True)
    localitate = models.ForeignKey(localitate.Localitate, models.DO_NOTHING)
    rata_prezenta = models.IntegerField()
    parola = models.CharField(max_length=64)
    cont_valid = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
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
        #send_mail(subject, body, sender, recipients, fail_silently=False)

        client_id = handled_cursor.callfunc("client_management.get_client_id", str, [data["email"]])
        handled_cursor.callproc("client_management.create_client_token", [client_id])
        auth_token = handled_cursor.callfunc("client_management.get_client_token", str, [client_id])
        return {"auth_token": auth_token}

    @staticmethod
    def generare_cod_inregistrare(data):
        handled_cursor = HandledCursor()
        parameters = []

        for param in data:
            parameters.append(data[param])
        handled_cursor.callproc("client_management.generare_cod_inregistrare", parameters)

        register_token = handled_cursor.callfunc("client_management.get_cod_inregistrare", str, [data["email"]])
        prenume_client = handled_cursor.callfunc("client_management.get_prenume", str, [data["email"]])

        subject = "Activare cont PROGRES"
        body = "Buna, " + prenume_client + ".\nLa cererea ta am generat un nou cod pentru activarea contului: " + register_token + "\nAi grija, expira in 3 ore.\n\nGanduri bune,\nEchipa Progres"
        sender = "progres@progres_app.com"
        recipients = [data["email"]]
        #send_mail(subject, body, sender, recipients, fail_silently=False)

    @staticmethod
    def validare_cont_client(data):
        handled_cursor = HandledCursor()
        parameters = []

        for param in data:
            parameters.append(data[param])
        handled_cursor.callproc("client_management.validare_cont_client", parameters)

    @staticmethod
    def login(data):
        handled_cursor = HandledCursor()
        parameters = []

        for param in data:
            parameters.append(data[param])
        handled_cursor.callproc("client_management.login", parameters)

        login_token = handled_cursor.callfunc("client_management.get_cod_login", str, [data["email"]])
        prenume_client = handled_cursor.callfunc("client_management.get_prenume", str, [data["email"]])
        subject = "Login in contul PROGRES"
        body = "Buna, " + prenume_client + ".\nFoloseste acest cod pentru accesarea contului tau: " + login_token + "\nAi grija, expira in 3 ore.\n\nGanduri bune,\nEchipa Progres"
        sender = "progres@progres_app.com"
        recipients = [data["email"]]
        # send_mail(subject, body, sender, recipients, fail_silently=False)

        client_id = handled_cursor.callfunc("client_management.get_client_id", str, [data["email"]])
        handled_cursor.callproc("client_management.create_client_token", [client_id])
        auth_token = handled_cursor.callfunc("client_management.get_client_token", str, [client_id])
        return {"auth_token": auth_token}

    @staticmethod
    def generare_cod_login(data):
        handled_cursor = HandledCursor()
        parameters = []

        for param in data:
            parameters.append(data[param])
        handled_cursor.callproc("client_management.generare_cod_login", parameters)

        register_token = handled_cursor.callfunc("client_management.get_cod_login", str, [data["email"]])
        prenume_client = handled_cursor.callfunc("client_management.get_prenume", str, [data["email"]])

        subject = "Activare cont PROGRES"
        body = "Buna, " + prenume_client + ".\nLa cererea ta am generat un nou cod pentru login: " + register_token + "\nAi grija, expira in 3 ore.\n\nGanduri bune,\nEchipa Progres"
        sender = "progres@progres_app.com"
        recipients = [data["email"]]
        #send_mail(subject, body, sender, recipients, fail_silently=False)

    @staticmethod
    def validare_login(data):
        handled_cursor = HandledCursor()
        parameters = []

        for param in data:
            parameters.append(data[param])
        handled_cursor.callproc("client_management.validare_login", parameters)

    @staticmethod
    def add_recenzie(data):
        handled_cursor = HandledCursor()
        parameters = []

        for param in data:
            parameters.append(data[param])
        handled_cursor.callproc("client_management.add_recenzie", parameters)

    @staticmethod
    def create_client_token(data):
        handled_cursor = HandledCursor()
        parameters = []

        for param in data:
            parameters.append(data[param])
        handled_cursor.callproc("client_management.create_client_token", parameters)

    @staticmethod
    def check_token(token, cont_valid, login_valid, client_id):
        handled_cursor = HandledCursor()
        parameters = [token, cont_valid, login_valid, client_id]
        result = handled_cursor.callfunc("client_management.check_token", str, parameters)
        return result

    @staticmethod
    def get_client_from_email(data):
        handled_cursor = HandledCursor()
        parameters = []
        for param in data:
            parameters.append(data[param])
        return_val = handled_cursor.callfunc("client_management.get_client_from_email", str, parameters)
        return return_val

    @staticmethod
    def get_salt(data):
        handled_cursor = HandledCursor()
        parameters = []
        for param in data:
            parameters.append(data[param])
        return_val = handled_cursor.callfunc("client_management.get_salt", str, parameters)
        return return_val