#55 - Ler 20 números e exibir qual foi o menor e o maior informados.

print("Informe 20 números.")
num = float(input())
maior = num
menor = num
for x in range(9):
    num = float(input())
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
print(f"O menor número é o {menor} e o maior número é o {maior}")