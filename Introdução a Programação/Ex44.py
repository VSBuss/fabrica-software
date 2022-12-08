#Faça um algoritmo que calcule e mostre a tabuada de um número digitado pelo usuário. 

x=1
num = int(input("Informe um número para calcular a tabuada: "))
while x<=10:
    print(f"{num} x {x} = {num*x}")
    x += 1
