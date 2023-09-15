import random
import time

class Conta:

    def __init__(self):
        self.id = random.randint(10000,99999999)
        print(f"O número da sua conta corrente será: {self.id}")
        self.nome = input("Nome: ")
        self.email = input("Email: ")
        self.endereco = input("Endereço: ")
        self.telefone = int(input("Telefone: "))
        self.senha = int(input("Senha numérica: "))
        self.saldo = 0

    def Editar_Dados(self, y):
        while True:
            if y == 1:
                print(f"Email antigo: {self.email}")
                self.email = input("Novo e-mail: ")
                return print("Alteração realizada com sucesso!")
            if y == 2:
                print(f"Endereço antigo: {self.endereco}")
                self.endereco = input("Novo endereço: ")
                return print("Alteração realizada com sucesso!")
            if y == 3:
                print(f"Telefone antigo: {self.telefone}")
                self.telefone = int(input("Novo telefone: "))
                return print("Alteração realizada com sucesso!")
            if y == 4:
                while True:
                    senha1 = input("Insira a nova senha: ")
                    senha2 = input("Confirme a nova senha: ")
                    if senha1 == senha2:
                        self.senha = senha2
                        print("Alteração realizada com sucesso!")
                        break
                    else:
                        print("As senhas não coincidem.")
                        continue
            if y == 5:
                return None
    def Sacar_Saldo(self):
        print(f"Você possui R${self.saldo}. Quanto deseja sacar?")
        while True:
            sacar = int(input("Informe a quantidade que deseja sacar: "))
            if (self.saldo - sacar) < 0:
                print("O valor não pode ser sacado.")
                continue
            else:
                print("As notas estão sendo contadas. Aguarde para retirar o dinheiro.")
                self.saldo = self.saldo - sacar
                time.sleep(2)
                return print("Saque realizado com sucesso!")
    def Depositar_Dinheiro(self, grana):
        self.saldo = self.saldo + grana
        return self.saldo
    def Listar_Dados(self):
        dados = {'Conta corrente':self.id, 'E-mail':self.email, 'Endereço':self.endereco, 'Telefone':self.telefone}
        return dados

class Conta2:

    def __init__(self, num_conta, nome, saldo)-> None:
        self.num_conta = num_conta
        self.nome = nome
        self.saldo = saldo

    
    def cadastrar(self) -> bool:
        try:
            self.num_conta = self.num_conta
            self.nome = self.nome
            self.saldo = self.saldo
        except:
            return False
        
    
    def depositar(self, saldo) -> bool:
        try:
            self.saldo += saldo
            return True
        except:
            return False


    def sacar(self, saque)-> bool:
        if(self.saldo<saque):
            print("Saldo insuficiente.")
            return False
        else:
            self.saldo -= saque
            print("Saque realizado com sucesso!")
            return True


    def listarDados(self)-> str:
        dados = {"Número da Conta: ":self.num_conta,
                 "Nome: ":self.nome,
                 "Saldo: ":self.saldo}
        return dados