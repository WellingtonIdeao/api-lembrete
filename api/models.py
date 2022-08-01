from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Lembrete(models.Model):
    class PrioridadeChoices(models.TextChoices):
        ALTA = 'ALTA', _('Alta')
        MEDIA = 'MEDIA', _('Media')
        BAIXA = 'BAIXA', _('Baixa')

    conteudo = models.CharField(max_length=100)
    arquivado = models.BooleanField(default=False)
    prioridade = models.CharField(max_length=5, choices=PrioridadeChoices.choices,
                                  default=PrioridadeChoices.BAIXA)
    criado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)


