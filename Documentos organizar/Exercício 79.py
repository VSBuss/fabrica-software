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
        print(f"{aluno.get('nome')}: {aluno.get('media'):.2f} ")
