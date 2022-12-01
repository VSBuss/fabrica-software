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