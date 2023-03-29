'''Fazer um programa para ler os dados de um funcionário (nome, salário bruto e imposto). Em
seguida, mostrar os dados do funcionário (nome e salário líquido). Em seguida, aumentar o salário
do funcionário com base em uma porcentagem dada (somente o salário bruto é afetado pela
porcentagem) e mostrar novamente os dados do funcionário.
Exemplo:
Nome: Joao Silva
Salário bruto: 6000.00
Imposto: 1000.00
Funcionário: Joao Silva, $ 5000.00
Digite a porcentagem para aumentar o salário: 10.0
Dados atualizados: Joao Silva, $ 5600.00
'''

#Uso de classes

class Funcionario:
    def __init__(self):
        self.nome = input("Nome: ")
        self.salariobruto = float(input("Salário bruto: "))
        self.imposto = float(input("Imposto: "))
        pass

    def mostrar_dados(self):
        print(f"Funcionário: {self.nome}, $ {self.salariobruto-self.imposto:.2f}")
    
    def aumentar_salário(self):
        porc = float(input("Digite a porcentagem para aumentar o salário: "))
        self.salariobruto = self.salariobruto * (1 + porc/100)
        print(f"Dados atualizados: {self.nome}, $ {self.salariobruto-self.imposto:.2f}")