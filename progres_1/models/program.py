from django.db import models
from progres_1.handled_cursor import HandledCursor
from progres_1.models import punct_lucru, zi_program


class Program(models.Model):
    id = models.IntegerField(primary_key=True)
    punct_lucru = models.ForeignKey(punct_lucru.PunctLucru, models.DO_NOTHING)
    zi_program_nr = models.ForeignKey(zi_program.ZiProgram, models.DO_NOTHING, db_column='zi_program_nr')
    ora_start = models.DecimalField(max_digits=10, decimal_places=6)
    ora_final = models.DecimalField(max_digits=10, decimal_places=6)

    class Meta:
        managed = False
        db_table = 'program'
        unique_together = (('punct_lucru', 'zi_program_nr', 'ora_start'),)

    @staticmethod
    def add_program(data):
        handled_cursor = HandledCursor()
        parameters = []

        for param in data:
            parameters.append(data[param])
        handled_cursor.callproc("tert_management.add_program", parameters)