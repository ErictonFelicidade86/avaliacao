from rest_framework.serializers import ModelSerializer
from core.models import Consulta
from regiao.api.serialazers import RegiaoSerialazer

class ConsultaSerialazer(ModelSerializer):
    regioes = RegiaoSerialazer()
    class Meta:
        model = Consulta
        fields = ('id', 'sigla', 'estado', 'regioes')