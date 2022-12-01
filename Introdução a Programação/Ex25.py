#p m g = 10 12 15

p = int(input("Informe a quantidade de camisetas pequenas: "))
m = int(input("Informe a quantidade de camisetas médias: "))
g = int(input("Informe a quantidade de camisetas grandes: "))
total = p*10 + m*12 + g*15
print(f"O valor total da compra é de R${total:.2f}.")