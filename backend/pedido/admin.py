from django.contrib import admin

# Register your models here.

from .models import Pedido, PedidoVisitar, PedidoAbastecer

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('codigo',)
    list_filter = ('status',)
    date_hierarchy = 'created'
