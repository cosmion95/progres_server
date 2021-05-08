from django.db import models

class ZiProgram(models.Model):
    nr_zi = models.IntegerField(primary_key=True)
    denumire = models.CharField(max_length=32)
    lucratoare = models.CharField(max_length=1)
    ordine = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'zile_program'