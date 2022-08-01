from rest_framework.viewsets import ModelViewSet
from .models import Lembrete
from .serializers import LembreteSerializer


class LembreteViewSet(ModelViewSet):
    queryset = Lembrete.objects.all()
    serializer_class = LembreteSerializer
