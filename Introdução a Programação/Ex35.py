tipo = input("Qual o tipo de carne: File Duplo, Alcatra ou Picanha? ")
qnt = float(input("Quantidade da carne: "))

tipo = tipo.upper()
itemcod = 0

if tipo == 'FILE DUPLO':
    if qnt > 5:
        ptotal = qnt * 35.8
    else:
        ptotal = qnt * 34.9
    itemcod = 1
elif tipo == 'ALCATRA':
    if qnt > 5:
        ptotal = qnt * 46.8
    else:
        ptotal = qnt * 44.9
    itemcod = 2
elif tipo == 'PICANHA':
    if qnt > 5:
        ptotal = qnt * 67.8
    else:
        ptotal = qnt * 66.9
    itemcod = 3
else:
    ptotal = 0
print("Qual o método de pagamento?\n"
"1 - Débito\n"
"2 - Crédito\n"
"3 - Cartão Loja\n"
"4 - PIX\n")
desc = '0%'
metodopg = int(input("Insira o número correspondente: "))
if metodopg == 1:
    metodopg = 'Débito'
elif metodopg == 2:
    metodopg = 'Crédito'
elif metodopg == 3:
    metodopg = 'Cartão Loja'
    ptotal = ptotal * 0.95
    desc = '5%'
else:
    metodopg = 'PIX'

print(f"\n\n\n\nHipermercado Tabajara LTDA\n"
f"Rua do Parque n° 75 QD 0001 LT 01\n"
f"Campo Grande - MS\n"
f"CNPJ 69.420.777/011-77      06/12/2022\n"
f"IE: 10.101.010-1        12:00:00\n"
f"IM: 12345678        CDD:987654\n"
f"---------------------------------------\n"
f"CUPOM FISCAL\n"
f"código/////descrição\n"
f"{itemcod}   {tipo} {qnt}KG\n"
f"Método de pagamento: {metodopg}\n"
f"Desconto: {desc}\n"
f"Total a pagar: {ptotal}\n"
f"---------------------------------------\n")
