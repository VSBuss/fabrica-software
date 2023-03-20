'''Fazer um programa para ler os valores da largura e altura de um retângulo. Em seguida, mostrar na tela o valor de
sua área, perímetro e diagonal.
Exemplo
Entre a largura e altura do retângulo:
3.00
4.00
AREA = 12.00
PERÍMETRO = 14.00
DIAGONAL = 5.00
'''
#Uso de classes
import math

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = 0
        self.altura = 0
    
    def area(self):
        print(f"Valor da área: {self.altura * self.largura}")
    
    def perimetro(self):
        print(f"Valor do perímetro: {self.largura * 2 + self.altura * 2}")

    def diagonal(self):
        print(f"Valor da diagonal: {math.sqrt(self.largura**2 + self.altura**2)}")