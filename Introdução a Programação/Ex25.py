#25 - Uma fábrica de camisetas produz os tamanhos pequeno, médio e grande, cada uma sendo vendida respectivamente por R$10,00, R$12,00 e R$15,00.
#Faça um algoritmo em que o usuário forneça a quantidade de camisetas pequenas, médias e grandes referentes a uma venda.
#O algoritmo deverá informar qual o valor total da compra.​

p = int(input("Informe a quantidade de camisetas pequenas: "))
m = int(input("Informe a quantidade de camisetas médias: "))
g = int(input("Informe a quantidade de camisetas grandes: "))
total = p*10 + m*12 + g*15
print(f"O valor total da compra é de R${total:.2f}.")