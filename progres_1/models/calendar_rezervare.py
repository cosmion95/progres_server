from django.db import models
from progres_1.models import punct_lucru, client, tip_rezervare, angajat
from progres_1.handled_cursor import HandledCursor


class CalendarRezervare(models.Model):
    id = models.IntegerField(primary_key=True)
    punct_lucru = models.ForeignKey(punct_lucru.PunctLucru, models.DO_NOTHING)
    client = models.ForeignKey(client.Client, models.DO_NOTHING)
    tip_rezervare = models.ForeignKey(tip_rezervare.TipRezervare, models.DO_NOTHING, blank=True, null=True)
    data_ora = models.DateField()
    validata = models.CharField(max_length=1)
    anulata = models.CharField(max_length=1)
    validata_de = models.IntegerField(blank=True, null=True)
    anulata_de = models.ForeignKey(angajat.Angajat, models.DO_NOTHING, db_column='anulata_de', blank=True, null=True)
    mesaj = models.CharField(max_length=256, blank=True, null=True)
    durata = models.IntegerField(blank=True, null=True)
    motiv_anulare = models.CharField(max_length=128, blank=True, null=True)
    prezenta = models.CharField(max_length=1)
    rezervare_la = models.IntegerField(blank=True, null=True)
    confirmata = models.CharField(max_length=1)
    confirmata_la = models.DateField(blank=True, null=True)
    creata_la = models.DateField()
    validata_la = models.DateField(blank=True, null=True)
    anulata_la = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'calendar_rezervari'

    @staticmethod
    def verifica_data_ora_rezervare(data):
        handled_cursor = HandledCursor()
        parameters = []

        for param in data:
            parameters.append(data[param])
        result = handled_cursor.callfunc("rezervare_management.verifica_data_ora_rezervare", str, parameters)
        return result

    @staticmethod
    def inregistrare_rezervare(data):
        handled_cursor = HandledCursor()
        parameters = []

        for param in data:
            parameters.append(data[param])
        handled_cursor.callproc("rezervare_management.inregistrare_rezervare", parameters)

    @staticmethod
    def validare_rezervare(data):
        handled_cursor = HandledCursor()
        parameters = []

        for param in data:
            parameters.append(data[param])
        handled_cursor.callproc("rezervare_management.validare_rezervare", parameters)

    @staticmethod
    def confirmare_rezervare_valida(data):
        handled_cursor = HandledCursor()
        parameters = []

        for param in data:
            parameters.append(data[param])
        handled_cursor.callproc("rezervare_management.confirmare_rezervare_valida", parameters)

    @staticmethod
    def anulare_client(data):
        handled_cursor = HandledCursor()
        parameters = []

        for param in data:
            parameters.append(data[param])
        handled_cursor.callproc("rezervare_management.anulare_client", parameters)

    @staticmethod
    def anulare_angajat(data):
        handled_cursor = HandledCursor()
        parameters = []

        for param in data:
            parameters.append(data[param])
        handled_cursor.callproc("rezervare_management.anulare_angajat", parameters)

    @staticmethod
    def marcare_neprezentat(data):
        handled_cursor = HandledCursor()
        parameters = []

        for param in data:
            parameters.append(data[param])
        handled_cursor.callproc("rezervare_management.marcare_neprezentat", parameters)