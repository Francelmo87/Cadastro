from django.contrib import admin

from .models import Titular, Endereco, Dependente


class DependenteInline(admin.TabularInline):
    model = Dependente
    extra = 0


class EnderecoInline(admin.TabularInline):
    model = Endereco
    extra = 0


@admin.register(Titular)
class UsuarioAdmin(admin.ModelAdmin):
    inlines = (DependenteInline, EnderecoInline,)
    list_display = ('nome', 'rg', 'cpf', 'nis', 'telefone', 'ativo',)