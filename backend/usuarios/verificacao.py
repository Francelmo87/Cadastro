from datetime import date

from .models import Titular


def verificar_titulares():
    hoje = date.today()

    # Filtra os titulares cuja validade já expirou e que ainda estão ativos
    titulares_expirados = Titular.objects.filter(ativo=True, dt_validade__lte=hoje)

    # Desativar os que estão fora da validade
    if titulares_expirados.exists():
        titulares_expirados.update(ativo=False)

    # Filtra os titulares que ainda estão no prazo e que estão inativos
    titulares_no_prazo = Titular.objects.filter(ativo=False, dt_validade__gt=hoje)

    # Ativar os titulares dentro do prazo
    if titulares_no_prazo.exists():
        titulares_no_prazo.update(ativo=True)