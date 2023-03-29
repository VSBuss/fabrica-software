'''Fazer um programa para ler as medidas dos lados de dois triângulos X e Y (suponha medidas
válidas). Em seguida, mostrar o valor das áreas dos dois triângulos e dizer qual dos dois triângulos
possui a maior área.
A fórmula para calcular a área de um triângulo a partir das medidas de seus lados a, b e c é a
seguinte (fórmula de Heron):

area = √p*(p-a)*(p-b)*(p-c) onde p=(a+b+c)/2
'''

#Uso de classes
import math
class Triangulo:
    def __init__(self):
        self.lado1 = float(input("Lado 1 do triângulo X: "))
        self.lado2 = float(input("Lado 2 do triângulo X: "))
        self.lado3 = float(input("Lado 3 do triângulo X: "))
        self.lado4 = float(input("Lado 1 do triângulo Y: "))
        self.lado5 = float(input("Lado 2 do triângulo Y: "))
        self.lado6 = float(input("Lado 3 do triângulo Y: "))
        pass
    
    def Area_triangulos(self):
        p1 = (self.lado1 + self.lado2 + self.lado3)/2
        area1 = math.sqrt(p1*(p1-self.lado1)*(p1-self.lado2)*(p1-self.lado3))

        p2 = (self.lado4 + self.lado5 + self.lado6)/2
        area2 = math.sqrt(p2*(p2-self.lado4)*(p2-self.lado5)*(p2-self.lado6))

        if area1 > area2:
            print("O triângulo X é o maior.")
        else:
            print("O triângulo Y é o maior.")