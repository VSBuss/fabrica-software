#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

letras = []
x = ''
qnt = 0
print("Digite 10 letras: ")
for i in range(10):
    x = input()
    if not x.isalpha():
        print("Você não digitou uma letra. ")
        continue
    else:
        letras.append(x)
    if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
        qnt += 1
print(f"Existem {qnt} consoante(s).")
print("As consoantes são:")
for i in range(10):
    if letras[i] == 'a' or letras[i] == 'e' or letras[i] == 'i' or letras[i] == 'o' or letras[i] == 'u':
        print(letras[i])
    else:
        continue