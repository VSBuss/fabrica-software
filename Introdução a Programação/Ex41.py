#41 - Três amigos, Joceyr, Thiago e Alexandre decidiram rachar igualmente a conta de um bar.
#Faça um algoritmo para ler o valor total da conta e imprimir quanto cada um deve pagar, mas faça com que Joceyr e Thiago não paguem centavos.
#Ex: uma conta de R$101,53 resulta em R$33,00 para Joceyr, R$33,00 para Thiago e R$35,53 para Alexandre.

conta = float(input("Informe o valor total da conta: "))
valortotal = conta
jt = conta//3 #divisão inteira sem considerar o resto
conta = conta - 2 * jt
print(f"A conta de R${valortotal} resulta em R${jt} para Joceyr e Thiago e R${conta} para Alexandre.")