'''Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".
'''

contador = 0
perguntas = ("Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?")
for x in range(5):
    resposta = input(f"{perguntas[0]} [S/N]: ")
    resposta = resposta.upper()
    if resposta == 'S':
        contador += 1
    elif resposta == 'N':
        continue
if contador == 1:
    print("Inocente.")
elif contador == 2:
    print("Suspeito.")
elif contador == 3 or contador == 4:
    print("Cúmplice.")
else:
    print("Assassino.")