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