#Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito.
#Foram obtidos os seguintes dados:​
#Código da cidade;​
#Número de veículos de passeio (em 1999);​
#Número de acidentes de trânsito com vítimas (em 1999). ​
#Deseja-se saber:​
#Qual o maior e menor índice de acidentes de transito e a que cidade pertence;​
#Qual a média de veículos nas cinco cidades juntas;​
#Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

macidente = 0
print("Informe os dados a seguir: ")
cod = int(input("\nCódigo da cidade: "))
vpa = int(input("Quantidade de veículos de passeio: "))
nat = int(input("Quantidade de acidentes de trânsito com vítimas: "))
maiori = nat
menori = nat
media = vpa
codigomaior = cod
codigomenor = cod
if vpa < 2000:
    macidente = macidente + nat

for i in range(4):
    cod = int(input("\nCódigo da cidade: "))
    vpa = int(input("Quantidade de veículos de passeio: "))
    nat = int(input("Quantidade de acidentes de trânsito com vítimas: "))
    media = media + vpa
    if vpa < 2000:
        macidente = macidente + nat
    if maiori < nat:
        maiori = nat
        codigomaior = cod
    if menori > nat:
        menori = nat
        codigomenor = cod
media = media / 5
print(f"\n\nA maior índice de acidentes de trânsito é de {maiori} na cidade {codigomaior}.")
print(f"O menor índice de acidentes de trânsito é de {menori} na cidade {codigomenor}.")
print(f"A média de veículos de passeio de todas as cidades é de {media:.2f}")
print(f"A média de acidentes de trânsito nas cidades com menos de 2000 veículos de passeio é de {macidente}")