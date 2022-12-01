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
