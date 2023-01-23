#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro de 1 a 10.
#O usuário deve informar de qual numero ele deseja ver a tabuada.
#A saída deve ser conforme o exemplo abaixo:​
#Tabuada de 5:​
#5 X 1 = 5​
#5 X 2 = 10​
#...​
#5 X 10 = 50

i = 1
tabuada = int(input("Informe um número inteiro de 1 a 10 para que eu calcule a tabuada deste.\n "))
print(f"Tabuada de {tabuada}")
while 1 <= i <= 10:
    print(f"{tabuada} X {i} = {tabuada * i }")
    i += 1
print("\n")
for x in range(tabuada, tabuada*11, tabuada):
    print(f"{tabuada} X {x/tabuada:.0f} = {x}")