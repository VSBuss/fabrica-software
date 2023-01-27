#Faça um Programa que peça as quatro notas de 10 alunos;
#Calcule e armazene num vetor a média de cada aluno;
#Imprima o número de alunos com média maior ou igual a 7.0.

nome = ''
alunos = {}
qntalunos = 0
for i in range(3):
    nome = input("Aluno: ")
    print("Informe as notas: ")
    media = nota = 0
    for x in range (4):
        nota = float(input())
        media = media + nota
    if media/4 >= 7:
        alunos[nome] = media/4
        qntalunos += 1
print(alunos)
print(f"{qntalunos} aluno(s) com média maior que 7.0.")