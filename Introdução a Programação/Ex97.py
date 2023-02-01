'''Crie um algoritmo para uma empresa de transportes que,
a partir do peso de uma encomenda fornecida pelo usuário calcule o preço da remessa conforme a seguinte tabela:

PESO DA ENCOMENDA                               VALOR
500 gramas ou menos                     R$1,10

Mais de 500 gramas, mas não             R$2,20
mais que 2KG

Mais de 2KG, mas não mais               R$3,70
que 10 KG

Mais de 10KG                            R$5,00 mais R$3,80/kg
                                        pelo peso que ultrapassar 10KG
'''
while True:
    peso = float(input("Informe o peso da encomenda em KG: "))
    if 0 < peso <= 0.5:
        total = 1.10
        break
    elif 0.5 < peso <= 2:
        total = 2.20
        break
    elif 2 < peso <= 10:
        total = 3.70
        break
    elif peso > 10:
        total = 5 + 3.8*(peso-10)
        break
    else: 
        print("\n>>>>INSIRA UM PESO VÁLIDO<<<<")
        continue
print(f"\nPeso da encomenda: {peso:.2f}KG\nValor total: R${total:.2f}")