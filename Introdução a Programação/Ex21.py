salario =  float(input("Digite o valor do salário: "))
venda = float(input("Digite o quanto o funcionário vendeu: "))

salfinal = salario + venda*0.04
print(f"O valor da comissão foi de R${venda*0.04:.2f} e o salário final foi de R${salfinal:.2f}.")