'''
Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande
quantidade de organizações:"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro

Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma.
O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados.
Não deverão ser aceitos valores além dos válidos para o programa (0 a 6).'''

print("Qual o melhor Sistema Operacional para o uso em servidores?\n"
"1- Windows Server\n"
"2- Unix\n"
"3- Linux\n"
"4- Netware\n"
"5- Mac OS\n"
"6- Outro\n\n")

votos = [0, 0, 0, 0, 0, 0]

while True:
    voto = int(input())
    if voto == 0:
        break
    match voto:
        case 1:
            votos[0] += 1
        case 2:
            votos[1] += 1
        case 3:
            votos[2] += 1
        case 4:
            votos[3] += 1
        case 5:
            votos[4] += 1
        case 6:
            votos[5] += 1
        case _:
            print("Voto inválido.")

print("Resultado dos votos respectivamente:\n"
f"1- Windows Server         {votos[0]}\n"
f"2- Unix                   {votos[1]}\n"
f"3- Linux                  {votos[2]}\n"
f"4- Netware                {votos[3]}\n"
f"5- Mac OS                 {votos[4]}\n"
f"6- Outro                  {votos[5]}")