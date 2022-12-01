valoraqui = float(input("Digite o valor de aquisição do produto: "))

if valoraqui < 50:
    valoraqui = valoraqui * 1.45
else:
    valoraqui = valoraqui * 1.3

print(f"Seu valor de venda será de {valoraqui:.2f}")
