from django.db import models
from progres_1.models import localitate, tert, domeniu
from progres_1.handled_cursor import HandledCursor
from rest_framework import serializers

class PunctLucru(models.Model):
    id = models.IntegerField(primary_key=True)
    tert = models.ForeignKey(tert.Tert, models.DO_NOTHING)
    denumire = models.CharField(max_length=128, blank=True, null=True)
    telefon = models.CharField(max_length=64, blank=True, null=True)
    domeniu = models.ForeignKey(domeniu.Domeniu, models.DO_NOTHING)
    localitate = models.ForeignKey(localitate.Localitate, models.DO_NOTHING)
    strada = models.CharField(max_length=128)
    nr_strada = models.CharField(max_length=16)
    cuvinte_cheie = models.CharField(max_length=256, blank=True, null=True)
    rata_prezenta_minima = models.IntegerField()
    minim_timp_estimat = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'puncte_lucru'

    @staticmethod
    def add_punct_lucru(data):
        handled_cursor = HandledCursor()
        parameters = []

        for param in data:
            parameters.append(data[param])
        handled_cursor.callproc("tert_management.add_punct_lucru", parameters)

    @staticmethod
    def get_puncte_lucru(data):
        handled_cursor = HandledCursor()
        parameters = []
        for param in data:
            parameters.append(data[param])
        return_val = handled_cursor.clobFunction("tert_management.get_puncte_lucru", parameters)
        return return_val

    @staticmethod
    def get_program_punct(data):
        handled_cursor = HandledCursor()
        parameters = []
        for param in data:
            parameters.append(data[param])
        return_val = handled_cursor.clobFunction("tert_management.get_program_punct", parameters)
        return return_val

    @staticmethod
    def get_urmatoarea_zi_lucratoare(data):
        handled_cursor = HandledCursor()
        parameters = []
        for param in data:
            parameters.append(data[param])
        return_val = handled_cursor.clobFunction("tert_management.get_urmatoarea_zi_lucratoare", parameters)
        return return_val

    @staticmethod
    def get_tipuri_rezervare(data):
        handled_cursor = HandledCursor()
        parameters = []
        for param in data:
            parameters.append(data[param])
        return_val = handled_cursor.clobFunction("tert_management.get_tipuri_rezervare", parameters)
        return return_val

    @staticmethod
    def get_procent_ocupare(data):
        handled_cursor = HandledCursor()
        parameters = []
        for param in data:
            parameters.append(data[param])
        return_val = handled_cursor.callfunc("tert_management.get_procent_ocupare", str, parameters)
        return return_val

    @staticmethod
    def get_program_neeligibil(data):
        handled_cursor = HandledCursor()
        parameters = []
        for param in data:
            parameters.append(data[param])
        return_val = handled_cursor.callfunc("tert_management.get_program_neeligibil", str, parameters)
        return return_val

    @staticmethod
    def verificare_timp_ales(data):
        handled_cursor = HandledCursor()
        parameters = []
        for param in data:
            parameters.append(data[param])
        return_val = handled_cursor.callfunc("rezervare_management.verificare_timp_ales", str, parameters)
        return return_val

class PunctLucruSerializer(serializers.ModelSerializer):
    class Meta:
        model = PunctLucru
        fields = ['denumire', 'telefon', 'strada', 'nr_strada']