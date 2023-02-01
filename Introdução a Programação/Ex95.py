'''Escrever um algoritmo para ler a quantidade de horas/aula de dois professores e o valor por hora recebido por cada um.
Mostrar na tela qual dos professores tem salário total maior.'''

horaaula = 65
qnthoras = 0
nome = ''
professores = []
for i in range(2):
    valor = 0
    nome = input("Nome: ")
    qnthoras = int(input("Quantidade de horas trabalhadas: "))
    valor = qnthoras * horaaula
    professor = {
        "Nome": nome,
        "Horas": qnthoras,
        "Valor": valor,
    }
    professores.append(professor)
if professores[0]['Valor'] > professores [1]['Valor']:
    print(f"{professores[0]['Nome']} ganha mais que {professores[1]['Nome']}")
else:
    print(f"{professores[1]['Nome']} ganha mais que {professores[0]['Nome']}")
print(f"O salário total de {professores[0]['Nome']} é R${professores[0]['Valor']} e o de {professores[1]['Nome']} é R${professores[1]['Valor']}")