from Contas import Conta
from Solicitacoes import Solicitacao
import csv

class pedido(Conta, Solicitacao):
    def __init__(self, nome, senha, codigo, tipo, descricao, gravidade):
        self.nome = nome
        self.senha = senha
        self.codigo = codigo
        self.tipo = tipo
        self.descricao = descricao
        self.gravidade = gravidade
        self.Defina_Nome(nome)
        self.Defina_Senha(self.senha)
        self.Defina_Area(self.codigo)
        self.tipo_solicitacao(self.tipo)
        self.descreva_solic(self.descricao, self.gravidade)
        self.conta_e_solicitacao(self.nome, self.tipo, self.descricao, self.gravidade)


    def conta_e_solicitacao(self, nome, tipo, descricao, gravidade):
        self.nome = nome
        self.tipo = tipo
        self.descricao = descricao
        self.gravidade = gravidade
        with open('dados.csv', 'w') as dados:
            writer = csv.writer(dados)
            header = (['nome', 'tipo', 'gravidade', 'descricao'])
            writer.writerow(header)

            writer.writerow([self.nome, self.tipo, self.gravidade, self.descricao])
