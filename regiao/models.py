from django.db import models

# Create your models here.

class Regiao(models.Model):
    sigla = models.CharField(max_length=2)
    regiao = models.CharField(max_length=255)

    def __str__(self):
        return self.regiao + '-' + self.sigla
