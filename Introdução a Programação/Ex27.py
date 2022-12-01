
alunos = 1
f = 0  #quantidade de alunas altas
m = 0  #total homens status regular ou ruim 4
sm = 0  #status masculino bom
x = 0.1

while alunos <= 50:
    matricula = int(input("\nNúmero da Matricula: "))
    sexo = input("Sexo: ")
    altura = int(input("Altura: "))
    if (sexo == 'f' or sexo == 'F') and altura > 170:
        f = f+1
    else:
        f = f
    stat = int(input("Status físico: "))
    if (sexo == 'm' or sexo == 'M') and stat == 1:
        sm = sm + 1
    elif (sexo == 'm' or sexo == 'M') and stat != 1:
        m = m +1
    else:
        m = m

    alunos = alunos + 1

porc = (sm*100)/(sm + m)

print("A quantidade de alunos do sexo feminino com altura maior que 170cm é de", f)
print("A porcentagem de alunos do sexo masculino em relação"
      " ao total de alunos do sexo masculino cujo o status físico seja bom é de", porc)
