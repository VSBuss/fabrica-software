#17 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhes contrataram para desenvolver o programa que calculará os reajustes.​
#Faça um programa que recebe o salário de um colaborador e reajuste-o seguindo o seguinte critério baseado no salário atual:​
#salários até R$ 280,00 (incluindo) : aumento de 20%​
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%​
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%​
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:​
#o salário antes do reajuste;​
#o percentual de aumento aplicado;​
#o valor do aumento;​
#o novo salário, após o aumento.​

salarioa = float(input("Digite o valor do salário atual do funcionário: "))
x = salarioa

if salarioa <= 280:
    salarioa = salarioa*1.2
    perc = 20
elif 280 < salarioa <= 700:
    salarioa = salarioa*1.15
    perc = 15
elif 700 < salarioa <= 1500:
    salarioa = salarioa*1.10
    perc = 10
else:
    salarioa = salarioa*1.05
    perc = 5
aumento = salarioa - x
print(f"O salário antes do reajuste era de R${x:.2f}, o percentual de "
      f"aumento aplicado foi de {perc}%, o valor do aumento foi de {aumento:.2f}R$ e"
      f" o valor do novo salário é de R${salarioa:.2f}.")
