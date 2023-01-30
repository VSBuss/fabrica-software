#Faça um programa que peça um numero inteiro positivo
#e em seguida mostre este numero invertido.​
#Exemplo:  12376489​
#    => 98467321​

num = int(input("Digite um numero inteiro positivo:  "))
num = str(num)
num = num[::-1]
print(num)