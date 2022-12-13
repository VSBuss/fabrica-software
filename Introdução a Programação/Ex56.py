#Escreva um algoritmo que leia 20 valores inteiros e ao final exiba:
#A soma dos números positivos.
#A quantidade de valores negativos.

x = 0
cont = 0
total = 0
print("Digite apenas números inteiros: ")
while x < 20:
    num = int(input())
    if num >= 0:
        total = total + num
    else:
        cont += 1
    x += 1
#O primeiro trecho de código, cont += 1, é o equivalente a fazer cont = cont + 1. O resultado dependerá de quem são x e 1.
#Se forem numéricos, serão somados; se forem strings serão concatenados (cont = Vitor e 1  ----> cont = Vitor1); se forem listas serão mescladas, etc.
#É o que chamamos de in-place operator.
#Em termos de API(Interface de Programação de Aplicação) do Python, fazer x += n é o mesmo que x = x.__iadd__(n)
#, ou seja, se x for instância de uma classe definida pelo usuário, o comportamento de += pode ser diferente do "esperado".
#Caso seja usado cont =+ 1 é o mesmo que cont = +(1); ou seja, está fazendo uma atribuição em x com o retorno do operador + em 1.
#Caso seja, cont=- -1 também retornará o valor 1 pois a função estará modificando o valor de 1 dessa forma: -(-1)
#Em cont=+ 1 se 1 for numérico, retornará o próprio valor sem modificar o sinal; se 1 for uma variável string dará erro.

print(f"A soma dos números positivos foi de {total} e a quantidade de números negativos foi de {cont}.")