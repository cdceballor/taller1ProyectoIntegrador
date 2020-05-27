from django.db import models
import uuid

class Temperatura(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(verbose_name='Tipo', max_length=20)
    value = models.IntegerField(verbose_name='Valor')
    lati = models.IntegerField(verbose_name='lati')
    longi = models.IntegerField(verbose_name='longi')
    tipTerr = models.TextField(max_length=140, verbose_name='tipTerr')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
# Create your models here.
