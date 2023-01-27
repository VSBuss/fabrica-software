 #Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
 #Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

vetor = []
par = []
impar = []
x = 0
print("Insira 20 números inteiros: ")
for i in range (20):
    vetor.append(int(input()))
    x = int(vetor[i])
    if vetor[i] % 2 == 0:
        par.append(vetor[i])
    else:
        impar.append(x)
print("Vetor original: ", vetor)
print("Vetor par: ", par)
print("Vetor ímpar: ", impar)