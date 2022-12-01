peso = float(input("Informe o peso dos peixes: "))
exc = 0
while peso >50:
    peso = peso -1
    exc = exc + 1

multa =  exc * 4

print(f"A quantidade em kg que excedem é de {exc}KG o valor da multa é de R${multa:.2f}.")