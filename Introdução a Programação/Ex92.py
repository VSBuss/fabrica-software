'''Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
Armazene os números numa biblioteca e separe-os por tipo.'''

num = []
par = []
impar = []
qntpar = qntimpar = 0
print("Informe 10 números inteiros: ")
for i in range(10):
    num.append(int(input(f"{i+1}° Número: ")))
for i in num:
    if i % 2 == 0:
        par.append(i)
        qntpar += 1
    else:
        impar.append(i)
        qntimpar += 1
numeros = {
    "Pares": par,
    "Impares": impar,
}
print(numeros)
print(f"Existem {qntpar} número(s) pare(s) e {qntimpar} número(s) ímpare(s)")