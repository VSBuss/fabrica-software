#14 - Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito.
#Após, calcule e escreva o saldo atual(saldo atual = saldo - débito + crédito).
#Também teste se saldo atual for maior ou igual a zero.
#Em seguida escreva a mensagem 'Saldo Positivo', senão, escrever a mensagem 'Saldo Negativo'.​

conta = int(input("Digite o número da conta do cliente: "))
print("Informe os valores à seguir.")
saldo = float(input("Saldo: "))
debito = float(input("Debito: "))
credito = float(input("Credito: "))

saldoatual = saldo - debito + credito
if saldoatual >= 0:
    print("Saldo Positivo.")
else:
    print("Saldo Negativo.")