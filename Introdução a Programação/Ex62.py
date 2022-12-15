#52- Ler diversos números e exibir quantos foram digitados.
#O valor -1 é código de  fim de entrada.

print("Insira diversos números e para parar a inserção digite '-1'")
num = 0
cont = 0

while num != -1:
    num = float(input())
    if num != -1:
        cont += 1
print(f"{cont} número(s) digitado(s)")
