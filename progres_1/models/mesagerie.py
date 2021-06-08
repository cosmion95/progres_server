from django.db import models
from progres_1.models import calendar_rezervare, client, angajat

class Mesagerie(models.Model):
    id = models.IntegerField(primary_key=True)
    rezervare = models.ForeignKey(calendar_rezervare.CalendarRezervare, models.DO_NOTHING)
    client = models.ForeignKey(client.Client, models.DO_NOTHING)
    angajat = models.ForeignKey(angajat.Angajat, models.DO_NOTHING, blank=True, null=True)
    mesaj = models.CharField(max_length=128, blank=True, null=True)
    citit_client = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'mesagerie'