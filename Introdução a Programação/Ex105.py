'''A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos.
Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários,
e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":

alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125

Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um
programa que gere um relatório, chamado "relatório.txt", no seguinte formato:

CME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB

O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória,
caso sejam necessários, de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco,
de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo programa principal.
O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.ios

'''
lista = []
nomes = []
porce = []
nome = ''
num = ''
arquivo = open('usuarios.txt', 'r')
for x in arquivo:
    lista.append(x)
arquivo.close()
num = len(lista)
for x in range(num):
    nome = lista[x]
    nome = nome[:15]
    nomes.append(nome)
for x in range(len(lista)):
    num = ''
    nome = lista[x]
    nome = nome[15:]
    for i in range(len(nome)):
        if nome[i].isnumeric():
            num = num + nome[i]
    nome = num
    lista[x] = nome
for x in range(len(lista)):
    lista[x] = int(lista[x])/1048576

mediamb = sum(lista)/len(lista)
mediamb = str(mediamb)
for x in range(len(mediamb)):
    num = ''
    num = mediamb[x]
    if num == ".":
        mediamb = mediamb[:x] + "," + mediamb[x+1:x+3]
        break

totalmb = str(sum(lista))

for x in range(len(totalmb)):
    num = ''
    num = totalmb[x]
    if num == ".":
        totalmb = totalmb[:x] + "," + totalmb[x+1:x+3]
        break
for x in range(len(lista)):
    porce.append(lista[x]*100/sum(lista))
for x in range(len(lista)):
    num = ''
    num = str(lista[x])
    for y in range(len(num)):
        if num[y] == ".":
            lista[x] = num[:y] + "," + num[y+1:y+3]
for x in range(len(lista)):
    num = ''
    num = lista[x]
    if len(num) != 7:
        num = " "*(7-len(num)) + num
    lista[x] = num
for x in range(len(porce)):
    num = 0
    num = round(porce[x], 2)
    porce[x] = str(num)
for x in range(len(porce)):
    num = ''
    num = porce[x]
    if len(num) != 5:
        num = " "*(5-len(num)) + num
    porce[x] = num

print("\nCME Inc.               Uso do espaço em disco pelos usuários\n"
"------------------------------------------------------------------------\n"
"Nr.  Usuário        Espaço utilizado     % do uso\n"
)
for x in range(len(nomes)):
    print(f"{x+1}   {nomes[x]} {lista[x]} MB             {porce[x]}%")
print(f"\nEspaço total ocupado: {totalmb} MB")
print(f"Espaço médio ocupado: {mediamb} MB\n")