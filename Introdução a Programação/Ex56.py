#Escreva um algoritmo que leia 20 valores inteiros e ao final exiba:
#A soma dos números positivos.
#A quantidade de valores negativos.

x = 0
cont = 0
print("Digite apenas números inteiros: ")
while x < 20:
    num = int(input())
    if num >= 0:
        total = total + num
    else:
        cont += 1
    x =+ 1
#O primeiro trecho de código, cont += 1, é o equivalente a fazer cont = cont + 1. O resultado dependerá de quem são x e n.
#Se forem numéricos, serão somados; se forem strings serão concatenados (cont = Vitor e 1  ----> cont = Vitor1); se forem listas serão mescladas, etc.
#É o que chamamos de in-place operator.
#Em termos de API(Interface de Programação de Aplicação) do Python, fazer x += n é o mesmo que x = x.__iadd__(n)
#, ou seja, se x for instância de uma classe definida pelo usuário, o comportamento de += pode ser diferente do "esperado".
#Já o segundo trecho, x =+ 1 é o mesmo que x = +1; ou seja, está fazendo uma atribuição em x com o retorno do operador + em 1.
#Se 1 for numérico, retornará o próprio valor sem modificar o sinal; se 1 for string dará erro.
#Em termos de API do Python, fazer +n é o mesmo que pos(n), que é o mesmo que n.__pos__(); ou seja, o valor retornado dependerá do método __pos__ do objeto.
#Também, se 1 for definido pelo usuário, o retorno de +1 pode ser diferente do "esperado".
#Todo esse comportamento é definido pela Data Model, em que é feita a transferência de responsabilidade da linguagem para o objeto.
#Não é o interpretador que definirá qual é o resultado do operador, mas sim o próprio objeto; ou seja, é possível você implementar estruturas que fogem completamente do esperado,
#como por exemplo -x retornando o dobro de x, +x retornando uma lista, etc.
print(f"A soma dos números positivos foi de {total} e a quantidade de números negativos foi de {cont}.")