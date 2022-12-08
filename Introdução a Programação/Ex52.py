#Escreva um algoritmo que leia 15 números inteiros e imprima apenas os números pares digitados.

x = 0
print("Digite apenas números inteiros:")
while x < 15:
    num = int(input())
    if num % 2 == 0:
        print(num)
    x += 1
