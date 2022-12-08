#Faça um algoritmo que imprima a tabuada de um número informado pelo usuário usando FOR.
tabuada = int(input("Insira um número para que eu mostre a tabuada dele: "))
for x in range(10):
    print(f"{tabuada} x {x+1} = {tabuada*(x+1)}")
