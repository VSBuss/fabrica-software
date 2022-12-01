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