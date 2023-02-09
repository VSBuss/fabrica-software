'''
Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões.
O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana.
Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470.
Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante
Desafio: Crie uma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.
'''
a = b = c = d = e = f = g = h = i = 0
lista = [a, b, c, d, e, f, g, h, i]
while True:
    vendas = float(input("Informe o valor das vendas brutas do vendedor: R$")) #800    -  9% = 72
    for x in range (9):
        if 200 + 100*x < 200 + vendas*0.09 <= 299 + 100*x:
            lista[x] += 1
        if vendas >= 200 + 100*x:
            lista[x] += 1
    if vendas == 0:
        break
print(lista)