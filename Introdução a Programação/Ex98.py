'''Máquina de café
Uma máquina de vender café funciona da seguinte forma:
o usuário seleciona um tipo de café, insere algumas notas ou moedas na máquina e
se a quantia paga for suficiente para pagar o café desejado a máquina enche um copo descartável com
o tipo de café selecionado e dá o troco em moedas. Faça um programa para imitar esse comportamento.

O usuário informa qual é o tipo de café desejado;
O usuário informa o valor pago;
O programa deve dizer qual deve ser o valor do troco e quantas moedas são necessárias para pagar esse troco.

Considere a existência de moedas com os seguintes valores: R$ 1.00, R$ 0.50, R$ 0.25, R$ 0.10, R$ 0.05 e R$ 0.01.

A tabela de preços é dada abaixo:

CAFÉ NORMAL     R$1,05
CAFÉ EXPRESSO   R$1,52
CAPUCCINO       R$2,17
MOCACCINO       R$2,36

'''
preços = (1.05, 1.52, 2.17, 2.36)
while True:
    cod = int(input('''1 - CAFÉ NORMAL     R$1,05
    \n2 - CAFÉ EXPRESSO   R$1,52
    \n3 - CAPUCCINO       R$2,17
    \n4 - MOCACCINO       R$2,36
    \n Selecione um número entre 1 a 4: '''))
    match cod:
        case 1:
            x = 0
            break
        case 2:
            x = 1
            break
        case 3:
            x = 2
            break
        case 4:
            x = 3
            break
    if cod < 1 or cod > 4:
        print("\n>>>>INSIRA UM CÓDIGO VÁLIDO<<<<\n")
        continue
dindin = float(input("Qual o valor pago? R$"))
if dindin > preços[x]:
    troco = dindin - preços[x]
    um = cinq = quarto = dez = cinco = um = 0

    while troco >= 1:
        um += 1
        troco = troco - 1
    while troco >= 0.50:
        cinq = cinq + 1
        troco = troco - 0.50
    while troco >= 0.25:
        quarto = quarto + 1
        troco = troco - 0.25
    while troco >= 0.10:
        dez = dez + 1
        troco = troco - 0.10
    while troco >= 0.05:
        cinco = cinco + 1
        troco = troco - 0.05
    print(f"O troco restante será de R${dindin - preços[x]:.2f} o caixa irá fornecer {um} moeda(s) de 1 real, "
    f"{cinq} moeda(s) de cinquenta centavos, {quarto} moeda(s) de vinte e cinco centavos, {dez} moeda(s) de dez centavos, "
    f"{cinco} moeda(s) de cinco centavos e {troco:.2f} moeda(s) de um centavo.")

else:
    print("A quantia inserida não é o suficiente. Aguarde para que a máquina devolva o seu dinheiro.")