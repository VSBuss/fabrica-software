#21 - Um funcionário recebe um salário fixo mais 4% de comissão sobre vendas.
#Faça um algoritmo que receba o salário fixo de um funcionário e o valor de suas vendas, calcule e mostre o valor da comissão e o salário final do funcionário.​

salario =  float(input("Digite o valor do salário: "))
venda = float(input("Digite o quanto o funcionário vendeu: "))

salfinal = salario + venda*0.04
print(f"O valor da comissão foi de R${venda*0.04:.2f} e o salário final foi de R${salfinal:.2f}.")