#Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados:
#valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
#
# Os juros e a quantidade de parcelas seguem a tabela abaixo:​
#Quantidade de Parcelas              % de Juros sobre o valor inicial da dívida​
#1                                                      0​
#3                                                      10​
#6                                                      15​
#9                                                      20​
#12                                                     25​
#
#​Exemplo de saída do programa:​
#Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela​
#R$ 1.000,00     0               1                       R$  1.000,00​
#R$ 1.100,00     100             3                       R$    366,00​
#R$ 1.150,00     150             6                       R$    191,67​

divida = float(input("Insira o valor da dívida: "))
juros = 0
x = 1
valor = divida

print("Valor da Dívida      Valor dos Juros     Quantidade de Parcelas      Valor da Parcela")
for i in range(1, 15, 3):

    #↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ Como deixar o código bonito ↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    string = f'R${valor:.2f}              ' 

    if juros < 10:
        string += f'0{juros}                  '
    else:
        string += f'{juros}                  '

    if (i-1) == 0:
        string += f'0{i}                           '        
    elif 0 < (i-1) < 10:
        string += f'0{i-1}                           '
    else:
        string += f'{i-1}                           '

    if i == 1:
         string += f'R${valor/i}'       
    else:
        string += f'R${valor/(i-1):.2f}'
    #↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑ Como deixar o. código bonito ↑↑↑↑↑↑↑↑↑↑↑↑↑

    print(string)
    juros = 7 + i + 2*x
    x += 1
    valor = divida + divida*juros/100