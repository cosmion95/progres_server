from django.db import models

from progres_1.handled_cursor import HandledCursor
from progres_1.models import judet


class Localitate(models.Model):
    id = models.IntegerField(primary_key=True)
    judet = models.ForeignKey(judet.Judet, models.DO_NOTHING)
    denumire = models.CharField(max_length=64)
    cod_postal = models.CharField(max_length=16)
    latitudine = models.DecimalField(max_digits=10, decimal_places=6)
    longitudine = models.DecimalField(max_digits=10, decimal_places=6)

    class Meta:
        managed = False
        db_table = 'localitati'
        unique_together = (('judet', 'denumire'),)

    @staticmethod
    def get_localitati(data):
        handled_cursor = HandledCursor()
        parameters = []
        for param in data:
            parameters.append(data[param])
        return_val = handled_cursor.clobFunction("nomenclatoare.get_localitati", parameters)
        return return_val