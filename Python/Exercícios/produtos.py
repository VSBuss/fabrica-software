class Mercado:
    def __int__(self):
        self.produtos = {'126': ['maçã kg', 5.99],
                         '257': ['pêra kg', 8.99],
                         '7897026001165': ['suco laranja natural 900ml', 9.99],
                         '7897510300125': ['agua sanitaria 1L', 7.99],
                         '7506339363883': ['creme dental 70g', 4.99],
                         '931': ['bacon fatiado kg', 39.99],
                         '7894904018246': ['coxinha da asa 1kg', 11.99],
                         '7898215151760': ['leite semidesnatado 1l', 3.99],
                         '99': ['bala de fruta un', 0.1],
                         '147': ['pão francês kg', 9.99]}
    def Valor_Total(self):
        nota_fiscal = nota_fiscal + ''
        return nota_fiscal
    def Calculo_Valor(self):
        a=a
    def Listar_Produtos(self)->str:
        for dados in self.produtos:
            for codigo in self.produtos[dados]:
                lista_de_produtos = codigo,'-'*(10-len(codigo)),self.produtos[dados][1],'\n'
        return lista_de_produtos