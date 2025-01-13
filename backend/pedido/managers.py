from django.db import models
from django.db.models import Q


class PedidoVisitarManager(models.Manager):
    def get_queryset(self):
        return super(PedidoVisitarManager, self).get_queryset().filter(Q(status='V') | (Q(status='P') & Q(tipo='V')))


class PedidoAbastecerManager(models.Manager):
    def get_queryset(self):
        return super(PedidoAbastecerManager, self).get_queryset().filter(Q(status='A') | (Q(status='P') & Q(tipo='A')), entregue=False)