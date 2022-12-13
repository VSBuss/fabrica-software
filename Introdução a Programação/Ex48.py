#48 - Elabore um algoritmo que calcule o que deve ser pago por um produto, considerando o preço normal de etiqueta e a escolha da condição de pagamento.
#Utilize os códigos da tabela a seguir para ler qual condição de pagamento escolhida e efetuar o cálculo adequado.
#Código Condição de pagamento:
#À vista em dinheiro ou pix, recebe 10% de desconto;​
#À vista no cartão de crédito, recebe 5% de desconto
#Parcelado em duas vezes, preço normal de etiqueta sem juros;
#Parcelado em três vezes, preço normal de etiqueta mais juros de 10%.

valor = float(input("Informe o valor do produto: "))
print("Selecione a forma de pagamento: ")
x = 0
while x == 0:
    pagt = int(input("\n1 - Dinheiro/PIX\n2 - Cartão de Crédito\n"))
    if pagt == 2:
        x = 1
        y = 0
        while y == 0:
            parc = int(input("\nDeseja parcelar em 1, 2 ou 3 vezes? "))
            if parc == 1:
                valor = valor * 0.95
                print(f"Valor a pagar: R${valor:.2f}")
                y = 1
            elif parc == 2:
                print(f"Valor a pagar: R${valor:.2f}")
                y = 1
            elif parc == 3:
                valor = valor * 1.1
                print(f"Valor a pagar: R$ {valor:.2f}")
                y = 1
            else:
                print("Quantidade do parcelamento inválida.")
    elif pagt == 1:
        valor = valor * 0.9
        print(f"Valor a pagar: R${valor:.2f}")
        x = 1
    else:
        print("Forma de pagamento inválilda.")