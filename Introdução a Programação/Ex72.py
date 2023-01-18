#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
#Ex.: 5!=5.4.3.2.1=120

num = int(input("Informe um número para que eu possa calcular o fatorial deste: "))
i = num
x = num
while i >= 1:
    x = x*i
    i = i - 1
print(f"O resultado do fatorial de {num} é {x}.")