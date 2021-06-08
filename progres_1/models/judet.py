from django.db import models
from progres_1.handled_cursor import HandledCursor


class Judet(models.Model):
    id = models.IntegerField(primary_key=True)
    denumire = models.CharField(unique=True, max_length=64)
    prescurtare = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'judete'

    @staticmethod
    def get_judete():
        handled_cursor = HandledCursor()
        return_val = handled_cursor.callfunc("nomenclatoare.get_judete", str, [])
        return return_val
