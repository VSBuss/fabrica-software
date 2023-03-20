'''Crie um função que recebe uma lista de números como parâmetro e retorne uma lista com apenas os números ímpares.'''

def ListaImpares(lista):
    impares = []
    for x in lista:
        if x % 2 == 1:
            impares.append(x)
    return impares

print(ListaImpares([1,2,3,4,5,6,7,8,9,10]))