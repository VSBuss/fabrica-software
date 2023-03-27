'''Crie uma função que recebe uma lista de números como parâmetro e retorne a média dos números.'''

def MediaLista(lista):
    soma = 0
    for x in lista:
        soma = soma + x
    return soma/len(lista)

print(MediaLista([2, 14, 15, 13, 16, 5, 14, 9, 10, 17]))