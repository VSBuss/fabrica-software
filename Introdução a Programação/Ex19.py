print("Informe os 3 lados de um triângulo: ")
lado1 = float(input("Lado 1: "))
lado2 = float(input("Lado 2: "))
lado3 = float(input("Lado 3: "))

if lado1+lado2<lado3 or lado1+lado3<lado2 or lado2+lado3<lado1:
    print("Esse triângulo não pode existir.")
else:
    if lado1 == lado2 == lado3:
        print("O triângulo é equilátero.")
    elif lado1 == lado2 != lado3 or lado1 == lado3 != lado2 or lado2 == lado3 != lado1:
        print("O triângulo é isósceles.")
    else:
        print("O triângulo é escaleno.")
