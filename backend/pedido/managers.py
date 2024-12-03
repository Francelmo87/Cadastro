from django.db import models


class PedidoVisitarManager(models.Manager):

    def get_queryset(self):
        return super(PedidoVisitarManager, self).get_queryset().filter(status='V')


class PedidoAbastecerManager(models.Manager):

    def get_queryset(self):
        return super(PedidoAbastecerManager, self).get_queryset().filter(status='A', entregue=False)