'''Escreva um algoritmo que solicite ao usuário a entrada de 5 números, e que exiba o somatório desses números na tela.
Após exibir a soma, o programa deve mostrar também os números que o usuário digitou, um por linha.'''

numeros = []
print("Insira 5 números: ")
for i in range(5):
    numeros.append(float(input()))
print(f"\nA soma dos números digitados é: {sum(numeros)}\nOs números digitados foram: ")
for i in range(5):
    print(numeros[i])