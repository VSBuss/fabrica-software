'''Cria uma função que recebe uma lista de string como parâmetro e retorna a string mais longa.'''

def StringMaior(lista):
    stringrandona = ''
    for x in lista:
        if len(stringrandona) < len(x):
            stringrandona = x
    return stringrandona

print(StringMaior(['Planeta', 'Abduzir', 'Esgoto', 'Torpedear', 'Suor', 'Censura', 'Alavanca', 'Preencher', 'Capataz', 'Palheiro', 'Eco', 'Hipopotomonstrosesquipedaliofobia']))