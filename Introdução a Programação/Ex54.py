#Faça o mesmo que o exercício anterior, porém, ao invés de ler 10 números, o programa deverá ler e somar números até que o valor digitado seja zero.

num = 1
total = 0
print("Digite números inteiros:")
while num != 0:
    num = int(input())
    total = total + num
print("O valor total da soma dos números digitados foi de", total)