#40 - João recebeu seu salário de R$ 1200,00 e precisa pagar duas contas (C1=R$ 200,00 e C2=R$120,00) que estão atrasadas.
#Como as contas estão atrasadas, João terá de pagar multa de 2% sobre cada conta.
#Faça um algoritmo que calcule e mostre quanto restará do salário do João.

c1 = 200 * 0.98
c2 = 120 * 0.98
restante = 1200-c1-c2

print(f"João terá de pagar R${c1+c2:.2f} e restará R${restante:.2f} de seu salário.")