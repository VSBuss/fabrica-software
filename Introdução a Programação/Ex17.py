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
