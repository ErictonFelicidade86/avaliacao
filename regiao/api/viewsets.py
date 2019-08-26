from rest_framework.viewsets import ModelViewSet
from regiao.models import Regiao
from .serialazers import RegiaoSerialazer

class RegiaoViewSet(ModelViewSet):
    queryset = Regiao.objects.all()
    serializer_class = RegiaoSerialazer