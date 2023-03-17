'''Fazer uma programa para ler os dados de duas pessoas, depois mostrar o nome da pessoa mais velha.'''
'''
pessoas = []
for x in range(2):
    print("Insira o nome e idade respectivamente: ")    
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    pessoa = {
        "nome": nome,
        "idade": idade,
    }
    pessoas.append(pessoa)
if pessoas[0]['idade'] > pessoas[1]['idade']:
    print(f"Pessoa mais velha: {pessoas[0]['nome']}")
else:
    print(f"Pessoa mais velha: {pessoas[1]['nome']}")
'''
class Pessoa:
    def __init__(self):
        self.nome = ''
        self.idade = 0