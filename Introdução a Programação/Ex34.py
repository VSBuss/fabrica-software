print("Álcool ou gasolina? ")
tipo = input("[A/G]: ")
tipo = tipo.upper()
qnt = float(input("Informe a quantidade em litros: "))

if tipo == 'A':
    if qnt > 20:
        valor = 1.9 * qnt * 0.95
    else:
        valor = 1.9 * qnt * 0.97
elif tipo == 'G':
    if qnt > 20:
        valor = 2.5 * qnt * 0.94
    else:
        valor = 2.5 * qnt * 0.96

print(f"O valor a ser pago pelo cliente é de R${valor:.2f}.")