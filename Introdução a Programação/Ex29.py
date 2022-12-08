#29 - Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:​
#Para homens: (72.7*h) - 58​
#Para mulheres: (62.1*h) - 44.7​

h = int(input("Informe a sua altura em cm: "))
homi = (72.7*h/100)-58
muie = (62.1*h/100)-44.7

print(f"Seu peso ideal é de {homi:.2f}kg caso você seja um homem e de {muie:.2f}kg caso você seja uma mulher.")