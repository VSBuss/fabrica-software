#49 - Elabore um programa que apresente o valor da conversão em real (R$) de um valor lido em dólar (US$).
#O programa deve solicitar o valor da cotação do dólar.​

cot = float(input("Qual o valor da cotação atual do dolar? "))
valor = float(input("Informe o valor em DOL a ser convertido em BRL: "))
valor = valor * cot
print (f"O valor convertido em real é de R${valor}")