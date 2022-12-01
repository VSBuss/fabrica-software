nome = input("Digite o nome do aluno: \n")
disciplina = input("Digite o nome da disciplina: \n")
nota1 = float(input("Informe o valor da nota da primeira prova: \n"))
nota2 = float(input("Informe o valor da nota da segunda prova: \n"))
nota3 = float(input("Informe o valor da nota da terceira prova: \n"))

if ((nota1 + nota2 + nota3) / 3) >= 6:
    print(f"O aluno {nome} foi aprovado na disciplina de {disciplina} e suas notas foram {nota1:.1f}, {nota2:.1f} e {nota3:.1f} respectivamente.")
else:
    print(f"O aluno {nome} foi reprovado na disciplina de {disciplina} e suas notas foram {nota1:.1f}, {nota2:.1f} e {nota3:.1f} respectivamente.")