#28 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:​
#O produto do dobro do primeiro com metade do segundo.​
#A soma do triplo do primeiro com o terceiro.​
#O terceiro elevado ao cubo.​

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro : "))
num3 = float(input("Digite um número real: "))

ex1 = (num1*2)*(num2/2)
ex2 = (num1*3)+num3
ex3 = num3 ** 3

print("",ex1,"\n",ex2,"\n",ex3)
