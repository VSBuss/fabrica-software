#Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito.
#Foram obtidos os seguintes dados:​
#Código da cidade;​
#Número de veículos de passeio (em 1999);​
#Número de acidentes de trânsito com vítimas (em 1999). ​
#Deseja-se saber:​
#Qual o maior e menor índice de acidentes de transito e a que cidade pertence;​
#Qual a média de veículos nas cinco cidades juntas;​
#Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

media = 0
mediaac = 0
print("Informe os dados a seguir: ")
for i in range(5):
    cod = int(input("\nCódigo da cidade: "))
    vpa = int(input("Quantidade de veículos de passeio: "))
    nat = int(input("Quantidade de acidentes de trânsito com vítimas: "))
    media = media + vpa
    if vpa < 2000:
        mediaac = mediaac + vpa
media = media / 5
print(f"A média de veículos de passeio de todas as cidades é de {media}")
print(f"A média de acidentes de trânsito nas cidades com menos de 2000 veículos de passeio é de {mediaac}")