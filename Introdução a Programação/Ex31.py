#31 - Faça um Programa que pergunte em que turno você estuda.
#Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.​

turno = input("Em que turno você estuda? Matutino, vespertino ou noturno?\n")
turno = turno.upper()

if turno == 'MATUTINO':
    print("Bom dia.")
elif turno == 'VESPERTINO':
    print("Boa tarde.")
elif turno == 'NOTURNO':
    print("Boa noite.")
else:
    print("Valor Inválido!")