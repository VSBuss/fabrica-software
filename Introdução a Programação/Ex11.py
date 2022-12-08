#Faça um algoritmo que o usuário possa digitar o seu nome e a sua idade.
#Utilizando uma tabela, verifique em qual item se enquadra a idade da pessoa e escreva em qual faixa etária a pessoa se encontra:​

nome = input("Digite o seu nome: \n")
idade = int(input("Digite a sua idade: \n"))

if (idade>= 0) and (idade<=2): #metodo alternativo
    print(f"{nome} está com {idade} e pela tabela é considerado um bebê.")
elif 3<=idade<=11:
    print(f"{nome} está com {idade} e pela tabela é considerado uma criança.")
elif 12<=idade<=21:
    print(f"{nome} está com {idade} e pela tabela é considerado um jovem.")
elif 22<=idade<=64:
    print(f"{nome} está com {idade} e pela tabela é considerado um adulto.")
elif 65<=idade<=100:
    print(f"{nome} está com {idade} e pela tabela é considerado um idoso.")
else:
    print(f"{nome} está com {idade} e pela tabela é considerado um velhinho.")