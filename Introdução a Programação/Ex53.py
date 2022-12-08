#Escreva um algoritmo que leia 10 números inteiros e, ao final, apresente a soma de todos os números lidos;
total = 0
x = 0
while x < 10:
    num = int(input("Digite um número inteiro: "))
    total = total + num
    x += 1
print("O valor total da soma dos números digitados foi de", total)