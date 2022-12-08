#42 - A fábrica de refrigerantes Gui-Cola vende seu produto em três formatos:
#Lata de 350 ml; Garrafa de 600 ml; Garrafa de 2 litros.
#Se um comerciante compra uma determinada quantidade de cada formato, faça um algoritmo para calcular quantos litros de refrigerante ele comprou.

print("Informe a quantidade comprada de cada item: ")
lata = int(input("Latas de 350ml: "))
garrafa = int(input("Garrafas de 600ml: "))
garrafa2l = int(input("Garrafas de 2 Litros: "))

total = lata*350 + garrafa*600 + garrafa2l*2000
total = total / 1000
print(f"Você comprou {total:.3f}litros de refrigerante.")