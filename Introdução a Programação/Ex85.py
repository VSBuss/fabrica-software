#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.​

numeros = []
print("Digite 10 números reais:")
for i in range (10):
    numeros.append(float(input()))
print("Aqui estão os números na ordem inversa:")
for i in range (-1,-11,-1):
    print(numeros[i])