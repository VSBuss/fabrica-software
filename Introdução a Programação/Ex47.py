#47 - Faça um algoritmo que leia dois valores inteiros A e B.
#Se os valores forem iguais deverá se somar os dois, caso contrário multiplique A por B.
#Ao final de qualquer um dos cálculos deve-se atribuir o resultado para uma variável C e mostrar seu conteúdo na tela. 

print("Informe o valor inteiro de duas variáveis A e B.")
a = int(input("A: "))
b = int(input("B: "))

if a == b:
    c = a+b
    print(f"A soma de A e B é {c}.")
else:
    c = a*b
    print(f"A multiplicação de A e B é = {c}.")
