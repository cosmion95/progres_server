from django.db import models


class Domeniu(models.Model):
    id = models.IntegerField(primary_key=True)
    denumire = models.CharField(max_length=128)

    class Meta:
        managed = True
        db_table = 'domenii'