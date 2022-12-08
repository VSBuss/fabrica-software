#Desenvolva um algoritmo que receba 1 número, o valor deverá ser lidos até que o usuário digite um número fora do intervalo de 1 a 100.
#Apresentar a mensagem “Dentro do Intervalo”, se for digitado um número fora do intervalo, o programa deverá imprimir “Fora do Intervalo” e encerrar o programa.

print("Digite um número:")
num = int(input())
while 1 <= num <= 100:
    print("Dentro do Intervalo")
    num = int(input())
print("Fora do Intervalo")