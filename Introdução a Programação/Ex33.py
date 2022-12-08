#33 - Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
#O resultado da operação deve ser acompanhado de uma frase que diga se o número é:​
#par ou ímpar;​
#positivo ou negativo;​
#inteiro ou decimal.​

print("Digite dois números:")
num1 = float(input(""))
num2 = float(input(""))
resultado = 0
print(f"Escolhe uma operação para realizar entre os números {num1} e {num2} respectivamente: ")
text = input("Soma, subtração, divisão ou multiplicação? ")
text = text.upper()

if text == 'SOMA' or text == '+':
    resultado = num1 + num2
elif text == 'SUBTRAÇÃO' or text == 'SUBTRACAO' or text == '-':
    resultado = num1 - num2
elif text == 'DIVISÃO' or text == 'DIVISAO' or text == '/':
    resultado = num1 / num2
elif text == 'MULTIPLICAÇÃO' or text == 'MULTIPLICACAO' or text == '*' or text == 'x':
    resultado = num1 * num2
else:
    print("Você digitou um valor inválido.")

print("O resultado é ",resultado)
if resultado % 2 == 0:
    print("O númera é par")
else:
    print("O número é ímpar")

if resultado >= 0:
    print("O número é positivo.")
else:
    print("O número é negativo.")

if type(resultado) == int:
    print("O número é inteiro.")
else:
    print("O número é decimal.")