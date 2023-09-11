from produtos import *

while True:
    qnt = input("Insira a quantidade: ")
    if qnt == '':
        notafiscal = Valor_Total()
    elif qnt == '?':
        Mercado.Listar_Produtos()
    else:
        qnt = float(qnt)
        qnt.Calculo_Valor()
        total = total + qnt
        codigo = int(input("Insira o código de barras: "))
valor_total = 20
print(f"Valor Total: {valor_total}")