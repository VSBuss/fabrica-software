'''DESENVOLVA  O  DIAGRAMA  DE  CLASSES  E IMPLEMENTE EM PYTHON, O SEGUINTE CASO:
UMA   CLASSE   PARA   REPRESENTAR   UMA CALCULADORA  QUE  REALIZA  AS  OPERAÇÕES BÁSICAS
(ADIÇÃO, SUBTRAÇÃO,MULTIPLICAÇÃO E DIVISÃO), CRIAR NO MÍNIMO DOIS OBJETOS.'''

class Calculadora:
    def __init__(self):
        self.num1 = float(input("Informe o 1° número: "))
        self.num2 = float(input("Informe o 2° número: "))
    
    def soma(self):
        return print(self.num1 + self.num2)
    def subt(self):
        return print(self.num1 - self.num2)
    def mult(self):
        return print(self.num1 * self.num2)
    def divi(self):
        return print(self.num1 / self.num2)

op1 = Calculadora()
op1.soma()
op1.subt()
op1.mult()
op1.divi()

op2 = Calculadora()
op2.soma()
op2.subt()
op2.mult()
op2.divi()