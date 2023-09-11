from conta import Conta2
import random

dados_conta = []

while True:
    opcoes = int(input("Banco Que Não Rouba Cliente 24/7\n"
                       "[1] - Cadastrar Nova Conta\n"
                       "[2] - Consultar Dados da Conta\n"
                       "[3] - Depositar\n"
                       "[4] - Sacar Dinheiro\n"
                       "[0] - Cancelar\n"
                       "Digite o número da opção desejada: "))
    match opcoes:
        case 0:
            break
        case 1:
            num_conta = random.randint(0000,1000)
            nome = input("Nome do Cliente: ")
            saldo = 0
            conta = Conta2(num_conta, nome, saldo)
            conta.cadastrar()
            dados_conta.append(conta)
            print(f"Número da conta cadastrada {num_conta}")
        case 2:
            num_conta = int(input("Informe o número da sua conta: "))
            for objeto in dados_conta:
                if(num_conta == objeto.num_conta):
                    mostrar_dados = objeto.ListarDados()
                    print(mostrar_dados)
        case 3:
            num_conta = int(input("Informe o número da conta: "))
            valor = float(input("Informe o valor a ser depositado: "))
            for objeto in dados_conta:
                if(num_conta == objeto.num_conta):
                    objeto.depositar(valor)
                    print(f"Você depositou R${valor:.2f} na conta concorrente de número {num_conta}")
        case 4:
            num_conta = int(input("Informe o número da conta: "))
            valor = float(input("Informe o valor a ser sacado: "))
            for objeto in dados_conta:
                if (num_conta == objeto.num_conta):
                    objeto.sacar(valor)
        case 5:
            break