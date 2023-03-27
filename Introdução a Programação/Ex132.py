'''DESENVOLVA  O  DIAGRAMA  DE  CLASSES  E IMPLEMENTE EM PYTHON, O SEGUINTE CASO:
UMA CLASSE CHAMADA "PESSOA" QUE TERÁ OS  SEGUINTES  ATRIBUTOS:  NOME,  IDADE  E  ALTURA.
ALÉM  DISSO,  TEREMOS  UM  MÉTODO  CHAMADO  "IMPRIMIR_INFORMACOES"  QUE  IRÁ  IMPRIMIR  OS
VALORES  DOS  ATRIBUTOS  DA  PESSOA  NA  TELA (CRIAR  NO  MÍNIMO  DOIS OBJETOS).'''

class Pessoa:
    def __init__(self):
        self.nome = input()
        self.idade = input()
        self.altura = input()
    def Imprimir_Informacoes(self):
        return print(f"Nome: {self.nome}\nIdade: {self.idade}\nAltura: {self.altura}")

p1 = Pessoa()
p1.Imprimir_Informacoes()

