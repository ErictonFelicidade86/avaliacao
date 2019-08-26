from django.db import models
from regiao.models import Regiao
# Create your models here.
class Consulta(models.Model):
    sigla = models.CharField(max_length=2)
    estado = models.CharField(max_length=255)
    regiao = models.ForeignKey(Regiao, on_delete=models.CASCADE, null=True, blank=True, name='regioes')

    def __str__(self):
        return self.estado + '-' + self.sigla
