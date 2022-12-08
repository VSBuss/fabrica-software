#5 - Faça um algoritmo que leia o nome do aluno, o nome da disciplina, notas de 3 provas e calcule a média desse aluno.​
#Posteriormente imprima o resultado de cada variável linha abaixo de linha.​

nome = input("Digite o nome do aluno: \n")
disciplina = input("Digite o nome da disciplina: \n")
nota1 = float(input("Digite a nota da primeira prova: \n"))
nota2 = float(input("Digite a nota da segunda prova: \n"))
nota3 = float(input("Digite a nota da terceira prova: \n"))

media = (nota1 + nota2 + nota3)/3

print("A média das notas é: ", media)
