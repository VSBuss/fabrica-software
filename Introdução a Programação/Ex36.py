from re import match
x = 1
while x > 0:
    print("Escolha um sanduíche: \n"
    "100 - Cachorro Quente\n"
    "101 - Ovo Simples\n"
    "102 - Bauru com Ovo\n"
    "103 - Hambúrguer\n")

    valortotal = 0
    cod = input("Insira o código do pedido: ")
    match(cod):
        case '100':
            valortotal += 11.20
        case '101':
            valortotal += 8.3
        case '102':
            valortotal += 11.5
        case '103':
            valortotal += 16.2

    print("\n\nEscolha uma bebida: \n"
    "201 - Refrigerante\n"
    "202 - Suco\n"
    "203 - Água Mineral\n")

    cod = input("Insira o código do pedido: ")
    match(cod):
        case '201':
            valortotal += 6
        case '202':
            valortotal += 7.5
        case '203':
            valortotal += 4.7

    print(f"O valor total a pagar é de R${valortotal}")

    print("Deseja fazer um novo pedido?")

    cond = input("[S/N]")
    cond = cond.upper()
    match(cond):
        case 'S':
            x = x
        case 'N':
            x -= 1
