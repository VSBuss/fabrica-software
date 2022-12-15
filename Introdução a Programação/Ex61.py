#51- Ler diversos números e exibir qual foi a soma.
#O valor -999 é o código de fim da entrada.

num = 0
total = 0
print("Informe diversos números para somar e insira '-999' para confirmar o fim da soma.")

while num != -999:
    num = float(input())
    if num != -999:
        total = total + num
print(f"O total da soma é {total}")