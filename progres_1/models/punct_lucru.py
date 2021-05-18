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

class PunctLucruSerializer(serializers.ModelSerializer):
    class Meta:
        model = PunctLucru
        fields = ['denumire', 'telefon', 'strada', 'nr_strada']