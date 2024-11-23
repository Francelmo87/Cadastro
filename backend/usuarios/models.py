from django.db import models
from django.urls import reverse_lazy
from backend.base.models import TimeStampedModel


class Titular(TimeStampedModel):
    nome = models.CharField('Nome', max_length=70, blank=True)
    rg = models.PositiveIntegerField('RG', null=True, blank=True)
    cpf = models.PositiveIntegerField('CPF', null=True, blank=True)
    nis = models.PositiveIntegerField('NIS', null=True, blank=True)
    telefone = models.PositiveIntegerField('Telefone', null=True, blank=True)
    dt_validade = models.DateField('Data da validade', null=True, blank=True)
    ativo = models.BooleanField('ativo', default=False)

    class Meta:
        verbose_name_plural = 'Titulares'
        ordering = ('nome',)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse_lazy('backend.usuarios:Titular_detail', kwargs={'pk': self.pk})


class Dependente(models.Model):
    nome = models.CharField('Nome', max_length=70, blank=True)
    cpf = models.PositiveIntegerField('CPF', null=True, blank=True)
    parentesco = models.CharField('Parentesco', max_length=20, blank=True)
    idade = models.PositiveIntegerField('Idade', null=True, blank=True)
    ocupacao = models.CharField('Ocupação', max_length=70, blank=True)
    renda = models.PositiveIntegerField('Renda', null=True, blank=True)
    titular = models.ForeignKey(
        Titular,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Dependentes'
        ordering = ('nome',)


class Endereco(models.Model):
    distrito = models.CharField('Distrito', max_length=20, blank=True)
    localidade = models.CharField('Localidade', max_length=20, blank=True)
    referencia = models.CharField('Ponto de referência', max_length=200, blank=True)
    titular = models.OneToOneField(
        Titular,
        on_delete=models.SET_NULL,
        null=True, 
        blank=True
    )

    class Meta:
        verbose_name_plural = 'Endereços'
        ordering = ('distrito',)

    def __str__(self):
        return self.distrito
    