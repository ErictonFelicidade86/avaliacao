from rest_framework.serializers import  ModelSerializer
from regiao.models import  Regiao



class RegiaoSerialazer(ModelSerializer):
    class Meta:
        model = Regiao
        fields = ('id', 'sigla', 'regiao')
