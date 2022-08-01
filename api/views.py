from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Lembrete
from .serializers import LembreteSerializer


class LembreteViewSet(ReadOnlyModelViewSet):
    queryset = Lembrete.objects.all()
    serializer_class = LembreteSerializer
