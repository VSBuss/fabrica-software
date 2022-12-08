#20 - Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

ano = int(input("Digite um ano para descobrir se é bissexto: "))

if ano % 4 != 0:
    print("O ano não é bissexto.")
else:
    print("O ano é bissexto.")
