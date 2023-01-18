#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

x = int(input("Informe dois números inteiros: \n"))
y = int(input())

t = 0

if x > y:
    t = y
    y = x
    x = t

t = x + 1

while t != y:
    print(t)
    t += 1