#Ex113 uso de classes

from Ex113 import *
class Ex114:
    if __name__ == "__main__":
        func1 = Funcionario()
        func2 = Funcionario()
        print("Dados do primeiro funcionário: ")
        func1.nome = input("Nome do 1° funcionário: ")
        func1.salario = int(input("Salário do 1° funcionário: "))

        print("Dados do segundo funcionário: ")
        func2.nome = input("Nome do 2° funcionário: ")
        func2.salario = int(input("Salário do 2° funcionário: "))

        media = (func1.salario + func2.salario)/2
        print(f"A média dos salários entre os dois funcionários é de: {media}")