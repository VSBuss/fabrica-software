class Conta:
    def __init__(self, receita_despesa, tipo, grupo, valor, data_cadastro, data_vencimento, data_pg, situacao) -> None:
        self.receita_despesa = receita_despesa
        self.tipo = tipo
        self.grupo = grupo
        self.valor = valor
        self.data_cadastro = data_cadastro
        self.data_vencimento = data_vencimento
        self.data_pg = data_pg        
        self.situacao = situacao
    
    def cadastrarConta(self)-> bool:
        try:
            self.receita_despesa = self.receita_despesa
            self.tipo = self.tipo
            self.grupo = self.grupo
            self.valor = self.valor
            self.data_cadastro = self.data_cadastro
            self.data_vencimento = self.data_vencimento
            self.data_pg = self.data_pg
            self.situacao = self.situacao
        except:
            return False