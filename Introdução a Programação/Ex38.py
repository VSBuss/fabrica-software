#38 - O restaurante Sabor em Quilo cobra R$59,00 por cada quilo de refeição.
#Escreva um algoritmo que leia o peso do prato montado pelo cliente (em quilos) e imprima o valor a pagar.
#Assuma que a balança já desconte o peso do prato.​

peso = float(input("Digite o valor do peso do prato em quilos: "))
print(f"O valor a ser pago pelo cliente é de R${peso*59:.2f}")