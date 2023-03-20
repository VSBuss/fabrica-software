'''Crie uma função que recebe uma lista de números como parâmetro e retorne o maior número da lista.'''

def MaiorNumLista(lista):
    maior = lista[0]
    for x in lista:
        if x >= maior:
            maior = x
    return maior

print(MaiorNumLista([1,2,3,4,5]))