import random

from conta import *

usuarios = []
while True:
    x = int(input("\n----Banco 24hrs----\n"
          "1-Criar Conta\n"
          "2-Editar Informações\n"
          "3-Sacar\n"
          "4-Depositar\n"
          "5-Sair\n"))

    if x == 1:
        usuarios.append(Conta())

    elif x == 2:
        numero_conta = int(input("Informe o número da sua conta: "))
        for count in usuarios:
            if(numero_conta == count.id):
                senha = int(input("Insira sua senha: "))
                if senha == count.senha:
                    dados = count.Listar_Dados()
                    print(dados)
                    y = int(input(f"\nOlá. Quais dados deseja alterar?\n"
                                  "1- Email\n"
                                  "2- Endereço\n"
                                  "3- Telefone\n"
                                  "4- Senha\n"
                                  "5- Cancelar\n"))
                    count.Editar_Dados(y)
                    break
                else:
                    print("Senha Inválida")
                    break
            else:
                continue
        else:
            print("Conta não encontrada.")
    elif x == 3:
        numero_conta = int(input("Informe o número da sua conta: "))
        for count in usuarios:
            if (numero_conta == count.id):
                senha = int(input("Insira sua senha: "))
                if senha == count.senha:
                    count.Sacar_Saldo()
                    break
                else:
                    print("Senha Inválida")
                    break
            else:
                continue
        else:
            print("Conta não encontrada.")
    elif x == 4:
        qnt = int(input("Insira a quantidade de dinheiro correspondente no envelope.\n"
                        "ATENÇÃO!\n"
                        "Não insira moedas. Insira apenas notas de papel moeda.\n"
                        "Valor: R$"))
        numero_conta = int(input("Informe o número da conta que deseja fazer o depósito: "))
        for count in usuarios:
            if (numero_conta == count.id):
                valoratual = count.Depositar_Dinheiro(qnt)
                print(f"Depósito feito com sucesso.\nVocê possui R${valoratual}\nRetire o comprovante de depósito indicado abaixo.\n")
                break
            else:
                continue
        else:
            print("Conta não encontrada.")

    elif x == 5:
        print("Tchau =)")
        exit()
    else:
        continue