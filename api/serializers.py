from rest_framework import serializers
from .models import Lembrete


class LembreteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lembrete
        fields = ['id', 'conteudo', 'arquivado', 'prioridade', 'modificado']