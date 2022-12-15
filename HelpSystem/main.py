from Contas import Conta
from Solicitacoes import Solicitacao


usuario01 = Conta("Gustavo",10000,"1000")

pedido01 = Solicitacao(1,"problemas de conexção", "Extrema Urgencia")

print(pedido01.descreva_solic("problema de conxção","Extrema Urgencia"))