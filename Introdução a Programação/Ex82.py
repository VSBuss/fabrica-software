'''Em uma competição de ginástica, cada atleta recebe votos de sete jurados.
A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes.
Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados
alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada
(retirar o melhor e o pior salto e depois calcular a média com as notas restantes).
As notas não são informados ordenadas.
Um exemplo de saída do programa deve ser conforme o exemplo abaixo:

Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:

Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04
'''
cond = ''
while True:
    soma = 0
    nota = []
    nome = input("Atleta: ")
    for i in range (7):
        nota.append(float(input(f"{i+1}° Nota: ")))
        if i == 0:
            maior = nota[i]
            menor = nota[i]
        soma = soma + nota[i]
        if nota[i] > maior:
            maior = nota[i]
        if nota[i] < menor:
            menor = nota[i]
    print("\nResultado final:\n"
    f"\nAtleta: {nome}"
    f"\nMelhor nota: {maior:.2f}"
    f"\nPior nota: {menor:.2f}"
    f"\nMédia: {(soma-maior-menor)/5:.2f}")
    cond = input("Digite 0 caso queira encerrar o programa. ")
    if cond == '0':
        break



''' Exercício abaixo foi feito por colega de sala. >>>>>>ESTUDAR<<<<<<
atletas = []
while True:
    nome = str(input("Digite o nome do atleta (ou enter para encerrar o programa): "))
    if nome == "":
        break
    atleta = {
        "nome": nome,
        "apresentações": [],
        "media": 0,
        "melhor_apresentação": 0,
        "pior_apresentação": 0,
    }
    for i in range(7):
        atleta.get("apresentações").append(float(input(f"Nota da {i+1}º apresentação: ")))
    atleta.get("apresentações").sort()                                                                     ".sort" - Deixa em ordem alfabetica e/ou numerica do menor pro maior
    atleta["pior_apresentação"] = atleta.get("apresentações").pop(0)                                       ".pop(0)" - Exclúi de uma biblioteca o primeiro valor registrado. 
    atleta["melhor_apresentação"] = atleta.get("apresentações").pop()                                      ".pop()" - Exclúi de uma biblioteca o última valor registrado.
    atleta["media"] = sum(atleta.get("apresentações")) / 5                                                 "sum()" - Soma
    print(f"\nMelhor apresentação: {atleta.get('melhor_apresentação'):.2f} "
        f"\nPior apresentação: {atleta.get('pior_apresentação'):.2f} "
        f"\nMédia dos demais apresentações: {atleta.get('media'):.2f} \n")
    atletas.append(atleta)

print("\n\nResultado final")
for atleta in atletas:
    print(f"{atleta.get('nome')}: {atleta.get('media'):.2f} ")'''