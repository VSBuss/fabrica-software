#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
#Imprima a idade e a altura na ordem inversa da ordem lida.

biblo = []
print("Informe idade e altura em cm de 5 pessoas: ")
for i in range (5):
    biblo.append(input(f"{i+}° pessoa: "))
