#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.​

n = int(input("Informe uma quantidade de números a ser informada: "))
print("Informe agora os números do conjunto: ")

num = float(input())
maior = num
menor = num
soma = num

while n > 1:
    num = float(input())
    soma = soma + num
    n -= 1
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
print(f"A soma dos valores digitados é de {soma}, o menor valor digitado é {menor} e o maior valor digitado é {maior}.")