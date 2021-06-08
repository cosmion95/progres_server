from django.db import models
from progres_1.models import client

class CodInregistrare(models.Model):
    id = models.IntegerField(primary_key=True)
    client = models.ForeignKey(client.Client, models.DO_NOTHING, blank=True, null=True)
    cod = models.CharField(max_length=6, blank=True, null=True)
    generat_la = models.DateField()
    generate_ultima_ora = models.IntegerField(blank=True, null=True)
    incercari_validare = models.IntegerField(blank=True, null=True)
    incercat_validare_la = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coduri_inregistrare'