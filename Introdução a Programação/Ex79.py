#Faça um programa que leia 5 números e informe a soma e a média dos números.​

soma = 0
media = 0
print("Informe 5 números.")
for x in range(5):
    num = int(input())
    soma = num + soma
media = soma/5
print(f"\nA soma dos números é {soma} e a média é {media:.2f}.")