'''Em uma eleição presidencial existem quatro candidatos.
Os votos são informados por meio de código. Os códigos utilizados são:

1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco

Faça um programa que calcule e mostre:

O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos.
Para finalizar o conjunto de votos tem-se o valor zero.'''

print("==========   TU ACREDITA NA DEMOCRACIA? KKKKKKKKKKKKK    ==========")
soma1 = soma2 = soma3 = soma4 = soma5 = soma6 = 0
while True:
    candidato = int(input("1 - José / 2 - João / 3 - Joel / 4 - Jean / 5 - Nulo / 6 - Em branco\n"))
    if candidato == 0:
        break
    if candidato == 1:
        soma1 += 1
    if candidato == 2:
        soma2 += 1
    if candidato == 3:
        soma3 += 1
    if candidato == 4:
        soma4 += 1
    if candidato == 5:
        soma5 += 1
    if candidato == 6:
        soma6 += 1
print(f"José recebeu {soma1} voto(s).\nJoão recebeu {soma2} voto(s).\nJoel recebeu {soma3} voto(s).\nJean recebeu {soma4} voto(s)."
f"\nO total de votos nulos foi de {soma5}.\nO total de votos em branco foi de {soma6}."
f"\nA percentagem de votos nulos sobre o total de votos é de {100*soma5/(soma1+soma2+soma3+soma4)}"
f"\nA percentagem de votos em branco sobre o total de votos é de {100*soma6/(soma1+soma2+soma3+soma4)}")