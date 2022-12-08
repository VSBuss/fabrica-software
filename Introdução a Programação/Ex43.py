#43 - Dani tem um cofrinho com muitas moedas, e deseja saber quantos reais conseguiu poupar.
#Faça um algoritmo para ler a quantidade de cada tipo de moeda, e imprimir o valor total economizado, em reais.
#Considere que existam moedas de 1, 5, 10, 25 e 50 centavos, e ainda moedas de 1 real.
#Não havendo moeda de um tipo, a quantidade respectiva é zero.

total = 0
for moeda in [1, 5, 10, 25, 50, 100]:
    qnt = int(input(f"Quantas moedas existem de {moeda} centavo(s)? "))
    total = total + (moeda * qnt)
print(f"O total economizado foi de R${total/100:.2f}")