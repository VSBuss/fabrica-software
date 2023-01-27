#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

nota = []
soma = 0
for i in range(4):
    nota.append(float(input(f"{i+1}° Nota: ")))
    soma = soma + nota[i]
print(f"A média das notas é {soma/4:.2f}")