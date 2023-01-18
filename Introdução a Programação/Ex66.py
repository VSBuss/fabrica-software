#O programa de fidelidade de uma determinada livraria premia seus clientes de acordo com o número de livros comprados a cada bimestre.

#Os pontos são atribuídos da seguinte forma:​
#•Se um cliente comprar 0 livros, ele ganhará 0 pontos;​
#•Se um cliente comprar um livro, ele ganhará 5 pontos;
#•Se um cliente comprar dois livros, ele ganhará 15 pontos;
#•Se um cliente comprar 3 livros, ele ganhará 30 pontos;
#•Se um cliente comprar 4 ou mais livros, ele ganhará 60 pontos.​

#Lista de brindes:​
#De 20 à 30 pontos o cliente poderá escolher entre: Uma EcoBag ou uma caneta personalizada​;
#De 35-60 pontos o cliente poderá escolher entre: Um livro (com valor máximo de R$30,00) ou Luminária de cabeceira.;
#Acima de 65 o cliente poderá escolher entre: 2 livros (com valor máximo de R$100,00) ou um powerbank.

pontos = 0
x = 1

while x != 0:
    x = int(input("Informe a quantidade de livros comprados pelo cliente: "))
    match(x):
        case 0:
            pontos += 0
        case 1:
            pontos += 5
        case 2:
            pontos += 15
        case 3:
            pontos += 30
    if x >= 4:
        pontos += 60

y = input(f"\nVocê possui {pontos} ponto(s).\nDeseja trocar seus pontos por brindes? (S/N) ")

print("\nAqui está uma lista com os brindes disponíveis:"
        "\n1 - 1 EcoBag por 20 pontos"
        "\n2 - 1 Caneta Personalizada por 30 pontos"
        "\n3 - 1 Livro (valor máximo de R$30,00) por 35 pontos"
        "\n4 - 1 Luminária de Cabeceira por 60 pontos"
        "\n5 - 2 Livros (valor máximo de R$100,00) por 65 pontos"
        "\n6 - 1 Powerbank por 65 pontos")
y = y.upper()

while y == 'S':        
    opc = int(input("\nEscolha uma das opções: "))
    match(opc):
        case 1:
            if pontos - 20 <0:
                print("Você não possui pontos suficientes para realizar essa troca.")
                y = input("Deseja selecionar outra opção de troca? (S/N) ")
            else:
                pontos -= 20
                print("Troca realizada com sucesso, retire seu brinde no caixa.")
                y = input("Deseja realizar outra troca? (S/N) ")
        case 2:
            if pontos - 30 <0:
                print("Você não possui pontos suficientes para realizar essa troca.")
                y = input("Deseja selecionar outra opção de troca? (S/N) ")
            else:
                pontos -= 30
                print("Troca realizada com sucesso, retire seu brinde no caixa.")
                y = input("Deseja realizar outra troca? (S/N) ")
        case 3:
            if pontos - 35 <0:
                print("Você não possui pontos suficientes para realizar essa troca.")
                y = input("Deseja selecionar outra opção de troca? (S/N) ")
            else:
                pontos -= 35
                print("Troca realizada com sucesso, retire seu brinde no caixa.")
                y = input("Deseja realizar outra troca? (S/N) ")
        case 4:
            if pontos - 60 <0:
                print("Você não possui pontos suficientes para realizar essa troca.")
                y = input("Deseja selecionar outra opção de troca? (S/N) ")
            else:
                pontos -= 60
                print("Troca realizada com sucesso, retire seu brinde no caixa.")
                y = input("Deseja realizar outra troca? (S/N) ")
        case 5:
            if pontos - 65 <0:
                print("Você não possui pontos suficientes para realizar essa troca.")
                y = input("Deseja selecionar outra opção de troca? (S/N) ")
            else:
                pontos -= 65
                print("Troca realizada com sucesso, retire seu brinde no caixa.")
                y = input("Deseja realizar outra troca? (S/N) ")
        case 6:
            if pontos - 65 <0:
                print("Você não possui pontos suficientes para realizar essa troca.")
                y = input("Deseja selecionar outra opção de troca? (S/N) ")
            else:
                pontos -= 65
                print("Troca realizada com sucesso, retire seu brinde no caixa.")
                y = input("Deseja realizar outra troca? (S/N) ")
    y = y.upper()