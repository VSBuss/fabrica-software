'''Crie uma função que recebe uma lista de números como parâmetro e retorne o número de ocorrências de um determinado número da lista.'''

def NumOcorrencia(lista):
    ocorrencias = 0
    for x in lista:
        if x == 6:
            ocorrencias += 1
    return ocorrencias

print(NumOcorrencia([9, 9, 4, 5, 6, 6, 2, 6, 10, 2]))