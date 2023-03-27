'''TESTE'''

x = int(input("Insira a idade de Roberto: "))

class Pessoa():
    def __init__(self, nome, idade, altura):
        self.idade = idade
        self.nome = nome
        self.altura = altura

        
    def exibirIdadeExtenso(self):
        exibir = ''
        idade = 0
        idade = self.idade
        if self.idade // 10 == 9:
            exibir = 'Noventa'
            idade = idade - 90
        elif self.idade // 10 == 8:
            exibir = 'Oitenta'
            idade = idade - 80
        elif self.idade // 10 == 7:
            exibir = 'Setenta'
            idade = idade - 70
        elif self.idade // 10 == 6:
            exibir = 'Sessenta'
            idade = idade - 60
        elif self.idade // 10 == 5:
            exibir = 'Cinquenta'
            idade = idade - 50
        elif self.idade // 10 == 4:
            exibir = 'Quarenta'
            idade = idade - 40
        elif self.idade // 10 == 3:
            exibir = 'Trinta'
            idade = idade - 30
        elif self.idade // 10 == 2:
            exibir = 'Vinte'
            idade = idade - 20
        if idade == 0:
            exibir = exibir + ' anos.'
        if idade == 1:
            exibir = exibir + ' e um anos.'
        if idade == 2:
            exibir = exibir + ' e dois anos.'
        if idade == 3:
            exibir = exibir + ' e três anos.'
        if idade == 4:
            exibir = exibir + ' e quatro anos.'
        if idade == 5:
            exibir = exibir + ' e cinco anos.'
        if idade == 6:
            exibir = exibir + ' e seis anos.'
        if idade == 7:
            exibir = exibir + ' e sete anos.'
        if idade == 8:
            exibir = exibir + ' e oito anos.'
        if idade == 9:
            exibir = exibir + ' e nove anos.'
        return print(exibir)

p1 = Pessoa('Roberto', x, 185)
print(p1.nome)
p1.exibirIdadeExtenso()
print(f"{p1.altura} centímetros de altura.")