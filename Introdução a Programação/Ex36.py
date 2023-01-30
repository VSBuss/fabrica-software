#36 - O cardápio da lanchonete Burgão é o seguinte:
#ESPECIFICAÇÃO           CÓDIGO              PREÇO ​
#Cachorro Quente          100               R$ 11,20 ​
#Ovo Simples              101               R$  8,30 ​
#Bauru com Ovo            102               R$ 11,50 ​
#Hambúrguer               103               R$ 16,20 ​
#Refrigerante             201               R$  6,00 ​
#Suco                     202               R$  7,50 ​
#Água Mineral             203               R$  4,70 ​
#Escreva um algoritmo que leia o código de um sanduíche e de uma bebida, e mostre o valor a pagar pelo cliente. Assuma as entradas corretas: ​

from re import match
x = 1
while x > 0: #desafio professora
    print("\nEscolha um sanduíche: \n"
    "100 - Cachorro Quente\n"
    "101 - Ovo Simples\n"
    "102 - Bauru com Ovo\n"
    "103 - Hambúrguer\n")
    
    valortotal = 0
    valorlanche = 0
    cod = input("Insira o código do pedido: ")
    match(cod):
        case '100':
            valorlanche += 11.20
        case '101':
            valorlanche += 8.3
        case '102':
            valorlanche += 11.5
        case '103':
            valorlanche += 16.2

    print("\n\nEscolha uma bebida: \n"
    "201 - Refrigerante\n"
    "202 - Suco\n"
    "203 - Água Mineral\n")

    cod = input("Insira o código do pedido: ")
    match(cod):
        case '201':
            valortotal = valorlanche + 6
        case '202':
            valortotal = valorlanche + 7.5
        case '203':
            valortotal = valorlanche + 4.7

    print(f"\nO valor total a pagar é de R${valortotal}")

    print("Deseja fazer um novo pedido?")

    cond = input("[S/N]")
    cond = cond.upper()
    if cond == 'S':
        x = x
    elif cond == 'N':
        x -= 1
    else:
        print("Valor inválido.")
    valortotal = 0