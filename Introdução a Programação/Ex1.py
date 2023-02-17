#1 - Faça um algoritmo que leia o nome, a idade, o sexo, o endereço e o telefone.​
#Posteriormente imprima o resultado de cada variável linha abaixo de linha.​

nome = input("Digite seu nome: \n")                              #O comando input() é usado para inserir dados em alguma variável
idade = input("Digite sua idade: \n")                            #Usar aspas dentro do input() permite a inserção de texto para personalizar a mensagem a ser exibida na tela
genero = input("Digite seu genero: \n")
endereco = input("Digite seu endereço: \n")
telefone = input("Digite seu telefone: \n")

print("", nome,"\n", idade,"\n", genero,"\n", endereco,"\n", telefone)           #Comando print() é usado para mostrar uma mensagem de texto na tela caso hajam aspas
                                                                                 #O que for separado por vírgula irá separar variáveis dos textos