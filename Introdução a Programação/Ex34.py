#34 - Um posto está vendendo combustíveis com a seguinte tabela de descontos:​

#Álcool:​
#até 20 litros, desconto de 3% por litro​
#acima de 20 litros, desconto de 5% por litro​

#Gasolina:​
#até 20 litros, desconto de 4% por litro​
#acima de 20 litros, desconto de 6% por litro ​

#Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina).
#Calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.​

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