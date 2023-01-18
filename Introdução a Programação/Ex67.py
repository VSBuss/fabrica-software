#Faça um algoritmo em que usuário escolha uma opção de​ acordo com o último número da placa do carro
#e mostre uma mensagem dizendo em que dia​ da semana não poderá circular.​
#0 - 1 “Não Circular 2ª Feira”​
#2 - 3 “Não Circular 3ª Feira”​
#4 - 5 “Não Circular 4ª Feira”​
#6 - 7 “Não Circular 5ª Feira”​
#8 - 9 “Não Circular 6ª Feira”

print("Informe a placa do carro: ")
placa = input()

ultimoChar = placa[-1]
ultimoChar = int(ultimoChar)
if 0 <= ultimoChar <= 1:
    print("Não Circular 2ª Feira")
elif 2 <= ultimoChar <= 3:
    print("Não Circular 3ª Feira")
elif 4 <= ultimoChar <= 5:
    print("Não Circular 4ª Feira")
elif 6 <= ultimoChar <= 7:
    print("Não Circular 5ª Feira")
elif 8 <= ultimoChar <= 9:
    print("Não Circular 6ª Feira")