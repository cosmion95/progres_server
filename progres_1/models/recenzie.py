from django.db import models
from progres_1.models import punct_lucru, client

class Recenzie(models.Model):
    id = models.IntegerField(primary_key=True)
    punct_lucru = models.ForeignKey(punct_lucru.PunctLucru, models.DO_NOTHING)
    client = models.ForeignKey(client.Client, models.DO_NOTHING)
    recenzie = models.CharField(max_length=256)
    creat_la = models.DateField()

    class Meta:
        managed = True
        db_table = 'recenzii'