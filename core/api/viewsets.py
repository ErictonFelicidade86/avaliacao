from rest_framework.viewsets import  ModelViewSet
from core.models import Consulta
from .serializers import ConsultaSerialazer

class ConsultaViewSet(ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerialazer