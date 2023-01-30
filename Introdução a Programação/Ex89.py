#Faça um Programa que peça as quatro notas de 10 alunos;
#Calcule e armazene num vetor a média de cada aluno;
#Imprima o número de alunos com média maior ou igual a 7.0.

alunos = []
nome = ''
qntalunos = 0
for i in range(10):
    nome = input("Aluno: ")
    aluno = {
        "Nome": nome,
        "Media": [],
    }
    print("Informe as notas: ")
    nota = 0
    for x in range (4):
        aluno.get('Media').append(float(input(f"{x+1}° Nota: ")))
    if sum(aluno.get('Media'))/4 >= 7:
        qntalunos += 1
    alunos.append(aluno)
for aluno in alunos:
    print(f"\nAluno: {aluno.get('Nome')}\nMédia: {sum(aluno.get('Media'))/4}")
print(f"\n{qntalunos} aluno(s) com média maior que 7.0.\n")




''' Exercício abaixo foi feito por colega de sala. >>>>>>ESTUDAR<<<<<<
alunos = []
while True:
    nome = str(input("Digite o nome do aluno (ou enter para encerrar o programa): "))
    if nome == "":
        break
    aluno = {
        "nome": nome,
        "notas": [],
        "media": 0,
    }
    for i in range(4):
        aluno.get("notas").append(float(input(f"{i+1}º Nota: ")))
    aluno.get("notas").sort()
    aluno["media"] = sum(aluno.get("notas")) / 4
    print(f"Média das Notas: {aluno.get('media'):.2f}")
    alunos.append(aluno)

print("Alunos com média maior que 7.0:")
for aluno in alunos:
    if aluno.get('media') >= 7.0:
        print(f"{aluno.get('nome')}: {aluno.get('media'):.2f} ")'''