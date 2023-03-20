'''Crie uma função que recebe uma lista de palavras como parâmetro e retorne uma lista com palavras que começam com a letra "A".'''

def PalavrasInicioA(lista):
    inicioA = []
    for x in lista:
        if x[0] == 'A' or x[0] == 'a':
            inicioA.append(x)
    return inicioA
print(PalavrasInicioA(['Planeta', 'Abduzir', 'Esgoto', 'Torpedear', 'Suor', 'Censura', 'Alavanca', 'Preencher', 'Capataz', 'Palheiro', 'Eco']))