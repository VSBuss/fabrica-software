'''DESENVOLVA  O  DIAGRAMA  DE  CLASSES  E IMPLEMENTE EM PYTHON, O SEGUINTE CASO:
UMA CLASSE TERÁ UM ATRIBUTO "RAIO" E DOIS MÉTODOS:
UM  PARA  CALCULAR  A  ÁREA  DO CÍRCULO  E  OUTRO  PARA  CALCULAR  O PERÍMETRO (CRIAR NO MÍNIMO DOIS OBJETOS).'''

class Circulo:
    def __init__(self):
        self.raio = float(input("Insira o valor do raio do círculo: "))

    def calculo_area(self):
        return print(f"Valor da área: {3.14*self.raio*self.raio:.2f}")
    
    def calculo_perimetro(self):
        return print(f"Valor do perímetro: {2*3.14*self.raio:.2f}")

circulo1 = Circulo()
circulo1.calculo_area()
circulo1.calculo_perimetro()

circulo2 = Circulo()
circulo2.calculo_area()
circulo2.calculo_perimetro()