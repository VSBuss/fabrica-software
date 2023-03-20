'''Crie uma função que recebe uma lista de números como parâmetro e retorne uma lista com apenas números pares.'''

def ListaPares(lista):
    pares = []
    for x in lista:
        if x % 2 == 0:
            pares.append(x)
    return pares

print(ListaPares([1,2,3,4,5,6,7,8,9,10]))