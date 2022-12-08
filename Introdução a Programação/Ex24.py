#24 - A lanchonete GostoSoft vende apenas um tipo de sanduíche, cujo recheio inclui duas fatias de queijo, uma fatia de presunto e uma rodela de hambúrguer.
#Sabendo que cada fatia de queijo ou presunto pesa 50 gramas, e que a rodela de hambúrguer pesa 100 gramas
#Faça um algoritmo em que o dono forneça a quantidade de sanduíches a fazer, e a máquina informe as quantidades (em quilos) de queijo, presunto e carne necessários para compra.​

quant = int(input("Informe a quantidade de hambúrgueres: "))
presunto = 0.05*quant
queijohamb = 0.1*quant

print(f"Será necessária a compra de {queijohamb}kgs de queijo, {presunto}kgs de presunto e {queijohamb}kgs de hambúrguer.")

