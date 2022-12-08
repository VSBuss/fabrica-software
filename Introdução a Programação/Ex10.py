#10 - Faça um algoritmo que verifique se o número digitado é menor, maior ou igual a 10 e apresente a mensagem referente ao número.​
numero = float(input("Informe um número: \n"))
if(numero == 10):
    print("O número é igual a dez.")
else:
    if(numero >10):
        print("O número é maior que dez.")
    else:
        print("O número é menor que dez.")