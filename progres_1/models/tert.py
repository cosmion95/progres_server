from django.db import models

class Tert(models.Model):
    id = models.IntegerField(primary_key=True)
    nume = models.CharField(max_length=64, blank=True, null=True)
    prenume = models.CharField(max_length=64, blank=True, null=True)
    email = models.CharField(unique=True, max_length=64, blank=True, null=True)
    username = models.CharField(max_length=32, blank=True, null=True)
    parola = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'terti'