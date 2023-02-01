#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

letras = []
x = ''
qnt = i = 0
print("Digite 10 letras: ")
while i < 10:
    x = input()
    if not x.isalpha(): #A função "isalpha serve para testar se a variavel atrelada a ela é uma letra ou não. Caso seja retorna True."
        print("Você não digitou uma letra. ")
    else:
        letras.append(x)
        i += 1
    if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
        qnt += 1
print(f"Existem {10-qnt} consoante(s).")
print("As consoantes são:")
for i in range(10):
    if not letras[i] in 'aeiou':
        print(letras[i])