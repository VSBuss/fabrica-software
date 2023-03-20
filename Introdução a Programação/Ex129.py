'''Crie uma função que recebe uma lista de números como parâmetro e retorne uma lista com apenas números menores que 10.'''

def MenorDez(lista):
    menores = []
    for x in lista:
        if x < 10:
            menores.append(x)
    return menores

print(MenorDez([2, 14, 15, 13, 16, 5, 14, 9, 10, 17]))