#Escreva um algoritmo que receba uma quantidade indeterminada de números,
#enquanto o numero for maior que 0 ou menor que 50, ao final imprima a quantidade de números digitados.

print("Digite um número:")
num = int(input())
cont = 1

while 0 < num < 50:
    num = int(input())
    cont += 1
print(f"O total de números digitados foi: {cont}")
