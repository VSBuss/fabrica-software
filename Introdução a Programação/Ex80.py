#Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
#No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados.
#O seu resultado fica sendo a média dos três valores restantes.
#Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos
#e depois informe a média dos saltos conforme a descrição acima informada
#(retirar o melhor e o pior salto e depois calcular a média).
#Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados.
#O programa deve ser encerrado quando não for informado o nome do atleta.
#A saída do programa deve ser conforme o exemplo abaixo:​
#
#Atleta: Rodrigo Curvêllo​
#Primeiro Salto: 6.5 m​
#Segundo Salto: 6.1 m​
#Terceiro Salto: 6.2 m​
#Quarto Salto: 5.4 m​
#Quinto Salto: 5.3 m​
#Melhor salto:  6.5 m​
#Pior salto: 5.3 m​
#Média dos demais saltos: 5.9 m​
#
#Resultado final:​
#Rodrigo Curvêllo: 5.9 m​

#USAR LISTA
nome = 'a'
while True:
    nome = input("Informe o nome do atleta: ")
    if nome == '':
        break
    posic = ["Primeiro", "Segundo", "Terceiro", "Quarto", "Quinto"]
    print("Informe os valores dos saltos realizados: ")
    soma = 0
    saltos = []
    for x in range(5):
        saltos.append(float(input()))
        if x == 0:
            maior = saltos[0]
            menor = saltos[0]        
        if saltos[x] > maior:
            maior = saltos[x]
        if saltos[x] < menor:
            menor = saltos[x]
        soma = soma + saltos[x]

    soma = soma - maior - menor
    soma = soma / 3

    print(f"\n\nAtleta: {nome}")
    for x in range(5):
        print(f"{posic[x]} Salto: {saltos[x]} m")

    print(f"Melhor salto: {maior} m"
    "Pior salto: {menor} m"
    "Média dos demais saltos: {soma}"
    "\nResultado final:"
    "{nome}: {soma}m")