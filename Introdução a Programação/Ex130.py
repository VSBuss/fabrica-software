'''Cria uma função que recebe uma lista de números como parâmetro e retorne o segundo menor número da lista.'''

def SegundoMenor(lista):
    lista.sort()
    return lista[1]

print(SegundoMenor([2, 14, 15, 13, 16, 5, 14, 9, 10, 17]))