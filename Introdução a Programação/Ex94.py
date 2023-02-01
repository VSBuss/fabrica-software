'''Escreva um algoritmo que leia um vetor com 10 posições de números inteiros.
Em seguida receba um novo valor do usuário e verifique se este valor se encontra no vetor.'''

numeros= []
print("Insira dez números inteiros em um vetor: ")
for i in range(10):
    numeros.append(int(input()))
num = int(input("Digite um número para verificar se ele foi salvo no vetor: "))
cont = numeros.count(num)
if cont > 0:
    print(f"O número {num} se encontra no vetor e foi digitado {cont} vez(es).")
else:
    print(f"O número {num} não foi digitado.")