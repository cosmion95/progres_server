from django.db import models
from progres_1.handled_cursor import HandledCursor
from progres_1.models import punct_lucru

class TipRezervare(models.Model):
    id = models.IntegerField(primary_key=True)
    denumire = models.CharField(max_length=64)
    validare_automata = models.CharField(max_length=1)
    durata = models.IntegerField()
    punct_lucru = models.ForeignKey(punct_lucru.PunctLucru, models.DO_NOTHING)
    creat_de = models.IntegerField()
    creat_la = models.DateField()

    class Meta:
        managed = True
        db_table = 'tipuri_rezervare'

    @staticmethod
    def add_tip_rezervare(data):
        handled_cursor = HandledCursor()
        parameters = []

        for param in data:
            parameters.append(data[param])
        handled_cursor.callproc("tert_management.add_tip_rezervare", parameters)