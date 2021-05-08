from django.db import models
from progres_1.handled_cursor import HandledCursor
from progres_1.models import punct_lucru

class Angajat(models.Model):
    id = models.IntegerField(primary_key=True)
    punct_lucru = models.ForeignKey(punct_lucru.PunctLucru, models.DO_NOTHING)
    nume = models.CharField(max_length=64, blank=True, null=True)
    prenume = models.CharField(max_length=64, blank=True, null=True)
    username = models.CharField(max_length=32, blank=True, null=True)
    telefon = models.CharField(max_length=64, blank=True, null=True)
    manager = models.CharField(max_length=1)
    parola = models.CharField(max_length=64)
    functie = models.CharField(max_length=64)

    class Meta:
        managed = True
        db_table = 'angajati'

    @staticmethod
    def add_angajat(data):
        handled_cursor = HandledCursor()
        parameters = []

        for param in data:
            parameters.append(data[param])
        handled_cursor.callproc("tert_management.add_angajat", parameters)
