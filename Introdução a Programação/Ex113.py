'''Fazer um programa para ler nome e salário de dois funcionários. Depois, mostre o salário médio dos funcionários.
Exemplo:
Dados do primeiro funcionário:
Nome: Carlos Silva
Salário: 6300.00
Dados do segundo funcionário:
Nome: Ana Marques
Salário: 6700.00
Salário médio = 6500.00
'''
#Uso de classes
class Funcionario:
    def __init__(self):
        self.nome = ''
        self.salario = 0