#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3%
#E que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
#Faça um programa que calcule e escreva o número de anos necessários
#Para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.​

A = 80000
B = 200000
x = 0

print(f"\nCrescimento anual de 3% no país A de {A} habitantes versus o crescimento anual de 1,5% no país B de {B} habitantes.")
#print(f"\nPaís A //// País B")
while A<B:
    #print(f"{A:.0f}     {B:.0f}")
    A = A * 1.03
    B = B * 1.015
    x += 1
print(f"Será necessário aproximadamente {x} anos para que a população de A ultrapasse B.") 