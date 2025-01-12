
from django.db import models

from backend.usuarios.models import Titular
from backend.base.models import TimeStampedModel

from .managers import PedidoVisitarManager, PedidoAbastecerManager

STATUS = (
    ('V', 'Visitar'),
    ('A', 'Abastecer'),
    ('P', 'Pendente'),
)


# Create your models here.
class Pedido(TimeStampedModel):
    titular = models.ForeignKey(
        Titular, 
        on_delete=models.SET_NULL,
        related_name='titulares', 
        null=True,
        blank=True,
        )
    cisterna = models.CharField('Nº Cisterna', max_length=10, null=True, blank=True)
    volume = models.PositiveIntegerField('Volume', null=True, blank=True)
    status = models.CharField('status', max_length=1, choices=STATUS, default='V')
    entregue = models.BooleanField('Entregue', default=False,  blank=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.titular.nome}'

    def codigo_formated(self):
        if self.pk:
            return str(self.pk).zfill(3)

class PedidoVisitar(Pedido):

    objects = PedidoVisitarManager()

    class Meta:
        proxy = True
        verbose_name = 'Pedido de visita'
        verbose_name_plural = 'Pedido de visita'


class PedidoAbastecer(Pedido):

    objects = PedidoAbastecerManager()

    class Meta:
        proxy = True
        verbose_name = 'Pedido para Abastecer'
        verbose_name_plural = 'Pedido para Abastecer'


class Motorista(models.Model):
    pedido = models.ManyToManyField(Pedido)
    dt_entrega = models.DateField(null=True, blank=True)
    nome = models.CharField(max_length=50, null=True, blank=True)
    placa = models.CharField(max_length=50, null=True, blank=True)
    km = models.FloatField()
    volume = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.nome
    