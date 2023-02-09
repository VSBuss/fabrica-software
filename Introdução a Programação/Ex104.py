'''Foram anotadas as idades e alturas de 30 alunos.
Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.'''

alunos = []
contador = media = 0
for i in range(30):
    print(f"\n{i+1}° Aluno:")
    idade = int(input("Idade: "))
    altura = int(input("Altura: "))
    media = media + altura
    aluno = {
        "idade": idade,
        "altura": altura,
    }
    alunos.append(aluno)
media = media/30
for i in range(30):
    if alunos[i]['idade'] > 13 and alunos[i]['altura'] < media:
        contador += 1
print(contador)