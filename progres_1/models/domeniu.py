from django.db import models
from progres_1.handled_cursor import HandledCursor

class Domeniu(models.Model):
    id = models.IntegerField(primary_key=True)
    denumire = models.CharField(max_length=128)

    class Meta:
        managed = True
        db_table = 'domenii'

    @staticmethod
    def get_domenii():
        handled_cursor = HandledCursor()
        return_val = handled_cursor.callfunc("nomenclatoare.get_domenii", str, [])
        return return_val