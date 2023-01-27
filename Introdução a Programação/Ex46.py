#46 - Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa.
#Caso sexo seja “F” e estado civil seja “CASADA? ( ͡° ͜ʖ ͡°)”, solicitar o tempo de casada (anos).

nome = input("Informe o nome: ")
sexo = input("Informe o sexo [M/F]: ")
estcivil = input("Informe o estado civil [SOLTEIRO(A)/CASADO(A)/VIUVO(A)]: ")

sexo = sexo.upper()
estcivil = estcivil.upper()
if sexo == 'F' and (estcivil == 'CASADO' or estcivil == 'CASADA'):
    aprovada = int(input("Está casada há quantos anos? "))
    print("Oi 😳 rsrs 😘")
else:
    print("Legal 👍")