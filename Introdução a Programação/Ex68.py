#Faça um algoritmo que mostre um Menu com opções de um cardápio de restaurante para uma pessoa.
#Coloque no mínimo 5 opções e máximo 10 opções de cardápio. Ex: Bife acebolado R$15,00; Lasanha R$25,00.​
#A pessoa vai escolher o prato desejado e após escolher o prato, o algoritmo deverá fazer a seguinte pergunta ao usuário:
#“Aceita pagar a gorjeta do garçom de 10% sobre o valor do prato?”
#Se o usuário aceitar, mostrar o valor final (valor do prato + 10%)
#Caso contrário, mostrar o valor final (somente o valor do prato).

valor = 0

print("\n                        RESTAURANTE TAURANTE\n\n\n"
"\n-------------------------------MENU-------------------------------"
"\n\n8-Galinhada de Presunto Caseiro e Queijo...................R$25,50"
"\n2-Pastel de Jaca ou Pastel de Queijo de Porco..............R$37,89"
"\n4-Espetinho de Frango Bovino com Tomate Roxo...............R$69,77"
"\n7-Toresmo de Pele de Cobra com Farinha de Pimentão.........R$93,51"
"\n3-Linguiça de Bacon Vegana com Espinafre Azedo.............R$49,28"
"\n5-Casca de Ovo Empanada ao Molho de Frutas Vermelhas.......R$37,93"
"\n1-Charque de Peixe ao Molho de Alface e Água Tônica Diet...R$99,71"
"\n6-Filé de Pé de Galinha Recheado com Bufalo Moído..........R$57,92\n\n")

prato = int(input("Escolha o prato desejado: "))
match(prato):
    case 8:
        valor = 15.5
    case 2:
        valor = 37.89
    case 4:
        valor = 69.77
    case 7:
        valor = 93.51
    case 3:
        valor = 49.28
    case 5:
        valor = 37.93
    case 1:
        valor = 99.71
    case 6:
        valor = 57.92

x = input("\nAceita pagar a gorjeta do garçom de 10% sobre o valor do prato? (S/N)  ")
x = x.upper()
if x == 'S':
    print(f"\nValor final: R${valor*1.1:.2f}")
else:
    print(f"\nValor final: R${valor}")