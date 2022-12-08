#32 - Faça um Programa para um caixa eletrônico.
#O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
#As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
#O programa não deve se preocupar com a quantidade de notas existentes na máquina.​
#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;​
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.​

sasuke = int(input("Informe o valor do saque: "))
valor = sasuke
cem = 0
cinq = 0
dez = 0
cinco = 0
um = 0


while sasuke >= 100:
    cem = cem + 1
    sasuke = sasuke - 100
while sasuke >= 50:
    cinq = cinq + 1
    sasuke = sasuke - 50
while sasuke >= 10:
    dez = dez + 1
    sasuke = sasuke - 10
while sasuke >= 5:
    cinco = cinco + 1
    sasuke = sasuke - 5

print(f"Para sacar a quantia de R${valor:.2f} o caixa irá fornecer {cem} no"
      f"ta(s) de cem reais, {cinq} nota(s) de cinquenta reais, {dez} nota(s) de dez reais, {cinco} nota(s) de cinco reais e {sasuke} nota(s) de um real.")
