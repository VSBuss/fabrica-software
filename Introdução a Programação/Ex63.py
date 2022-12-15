#53 - Ler diversos números e exibir quantos números ímpares foram digitados.
#Considere o valor - 999 como código fim de entrada.

print("Insira diversos números e para parar digite -999")
num = 0
cont = 0

while num != -999:
    num = float(input())
    if num%2!=0 and num!=-999:
        cont += 1
print(f"{cont} número(s) ímpar(es)")