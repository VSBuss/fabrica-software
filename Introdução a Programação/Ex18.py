#18 - Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do
#Imposto de Renda, que depende do salário bruto (conforme tabela abaixo);
#3% para o Sindicato;
#FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
#O Salário Líquido corresponde ao Salário Bruto menos os descontos.
#O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.​

#Desconto do IR:​
#Salário Bruto até 900 (inclusive) - isento​
#Salário Bruto até 1500 (inclusive) - desconto de 5%​
#Salário Bruto até 2500 (inclusive) - desconto de 10%​
#Salário Bruto acima de 2500 - desconto de 20% 

#Imprima na tela as informações, dispostas conforme o exemplo abaixo.
#No exemplo o valor da hora é 5 e a quantidade de hora é 220.​
#Salário Bruto: (5 * 220)        : R$ 1100,00​
#(-) IR (5%)                     : R$   55,00  ​
#(-) INSS ( 10%)                 : R$  110,00​
#FGTS (11%)                      : R$  121,00​
#Total de descontos              : R$  165,00​
#Salário Liquido                 : R$  935,00​

vhora = float(input("Informe o valor pago pela hora trabalhada: R$"))
quant = float(input("Informe a quantide de horas trabalhadas: "))

salb = vhora * quant

if salb <= 900:
    ir = 0
    inss = salb*0.10
    sindlixo = salb*0.03
    fgts = salb*0.11
    porc = 0
elif 900<salb<=1500:
    ir = salb*0.05
    inss = salb*0.10
    sindlixo = salb*0.03
    fgts = salb*0.11
    porc = 5
elif 1500<salb<=2500:
    ir = salb*0.1
    inss = salb*0.10
    sindlixo = salb*0.03
    fgts = salb*0.11
    porc = 10
else:
    ir = salb*0.2
    inss = salb*0.10
    sindlixo = salb*0.03
    fgts = salb*0.11
    porc = 20

totaldesc = ir + inss + sindlixo
sall = salb - totaldesc

if salb>900:
    print(f"Salário Bruto: ({vhora}*{quant})        :R${salb:.2f}\n"
    f"(-)IR ({porc}%)                      :R${ir:.2f}\n"
    f"(-)INSS (10%)                   :R${inss:.2f}\n"
    f"(-)Sindicato(3%)                :R${sindlixo:.2f}\n"
    f"FGTS(11%)                       :R${fgts:.2f}\n"
    f"Total de Descontos:             :R${totaldesc:.2f}\n"
    f"Salário Líquido:                :R${sall:.2f}")
else:
    print(f"Salário Bruto: ({vhora}*{quant})        :R${salb:.2f}\n"
          f"(-)INSS (10%)                   :R${inss:.2f}\n"
          f"(-)Sindicato(3%)                :R${sindlixo:.2f}\n"
          f"FGTS(11%)                       :R${fgts:.2f}\n"
          f"Total de Descontos:             :R${totaldesc:.2f}\n"
          f"Salário Líquido:                :R${sall:.2f}")