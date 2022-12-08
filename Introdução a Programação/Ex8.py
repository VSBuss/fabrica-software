#8 - Faça um algoritmo que calcule o custo estimado de uma viagem de carro.​
#Posteriormente imprima o resultado.​

distancia = float(input("Informe a distância em kilometros de sua ultima viagem: \n"))
valor = float(input("Informe o valor cobrado pelo litro do combustivel: \n"))
kmporlitro = float(input("Informe quantos kilometros por litro seu carro faz: \n"))

custo = distancia/kmporlitro*valor

print(f"O custo estimado da última viagem foi de {custo:.2f} reais")