'''Faça um algoritmo que receba o valor do salário de uma pessoa e o valor de um financiamento pretendido.
Caso o financiamento seja menor ou igual a 5 vezes o salário da pessoa, o algoritmo deverá escrever “Financiamento Concedido".
Senão, ele deverá escrever "Financiamento Negado".
Independente de conceder ou não o financiamento, o algoritmo escreverá depois a frase "Obrigado por nos consultar."
'''
salario = int(input("Informe o valor do seu salário: R$"))
financ = int(input("Informe o valor do financimento pretendido: R$"))

if financ <= 5*salario:
    print("Financiamento Concedido")
else:
    print("Financiamento Negado")
print("Obrigado por nos consultar.")