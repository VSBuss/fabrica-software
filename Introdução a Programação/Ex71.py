#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

par = 0
impar = 0
print("Informe 10 números inteiros:")
for i in range(10):
    x = int(input())
    if x % 2 == 0:
        par += 1
    else:
        impar += 1
print(f"Existem {par} número(s) par(es) e {impar} número(s) ímpar(es).")