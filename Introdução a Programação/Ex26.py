#26 - Um brechó revende produtos usados, e fixa o preço de venda de cada produto conforme o valor de sua aquisição:
#Se o preço de aquisição de um produto é menor que R$ 50,00, ele deve ser vendido por um preço 45% maior, caso contrário o lucro será de 30%.
#Sabendo disso, faça um algoritmo que leia o valor de aquisição de um produto e mostre o seu valor de venda.​

valoraqui = float(input("Digite o valor de aquisição do produto: "))

if valoraqui < 50:
    valoraqui = valoraqui * 1.45
else:
    valoraqui = valoraqui * 1.3

print(f"Seu valor de venda será de {valoraqui:.2f}")
