from django.db import models
from progres_1.handled_cursor import HandledCursor
from progres_1.models import punct_lucru


class ExceptieProgram(models.Model):
    id = models.IntegerField(primary_key=True)
    punct_lucru = models.ForeignKey(punct_lucru.PunctLucru, models.DO_NOTHING)
    data = models.DateField()
    ora_start = models.DecimalField(max_digits=10, decimal_places=6)
    ora_final = models.DecimalField(max_digits=10, decimal_places=6)

    class Meta:
        managed = True
        db_table = 'exceptii_program'

    @staticmethod
    def add_exceptie_program(data):
        handled_cursor = HandledCursor()
        parameters = []

        for param in data:
            parameters.append(data[param])
        handled_cursor.callproc("tert_management.add_exceptie_program", parameters)