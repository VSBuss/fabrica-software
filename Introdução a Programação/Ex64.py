#54- Ler diversos números inteiros e exibir quantas vezes o número 50 foi  informado.
#O valor 0 é o código de fim de entrada. 

num = 1
cont = 0
print("Insira diversos números inteiros e digite o número '0' para parar")

while num != 0:
    num = int(input())
    if num == 50:
        cont += 1
print(f"O número 50 foi digitado {cont} vez(es).")