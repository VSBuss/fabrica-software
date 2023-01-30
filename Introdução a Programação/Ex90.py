#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
#Imprima a idade e a altura na ordem inversa da ordem lida.

pessoas = []
nome = ''
altura = ''
idade = ''

for i in range(5):
    nome = input("\nNome: ")
    idade = input("Idade: ")
    altura = input("Altura em cm: ")
    pessoa = {
        "Nome": nome,
        "Idade": idade,
        "Altura": altura,
    }
    pessoas.append(pessoa)
print("\n")
for i in range(-1, -6, -1):
    print(pessoas[i])



# NÃO ENTENDI O ENUNCIADO E FIZ ESSA JOÇA
''' for pessoa in pessoas:
    teste = ''
    reverse = ''
    teste = list(reversed(pessoa.get('Idade')))
    for i in teste:
        reverse += i
    print(f"\nNome: {pessoa.get('Nome')}\nIdade: {reverse}")
    reverse = ''
    teste = list(reversed(pessoa.get('Altura')))
    for i in teste:
        reverse += i
    print(f"Altura: {reverse}") '''