'''Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).'''

temp = []
print("Insira o valor da temperatura de 12 meses: ")
for i in range(12):
    temp.append(float(input(f"{i+1}° mês: ")))
print(f"Média: {sum(temp)/12:.2f}")
lista = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
for i in range(12):
    if temp[i]>sum(temp)/12:
        print(f"{i+1} - {lista[i]}")