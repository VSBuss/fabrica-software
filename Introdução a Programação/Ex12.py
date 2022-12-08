#12 - Faça um algoritmo que verifique se o número digitado é positivo ou negativo.​
numero = float(input("Digite um número: "))
if numero > 0:
    print("O número é positivo.")
elif numero == 0:
    print("O número é igual a zero.")
else:
    print("O número é negativo.")