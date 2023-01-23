#Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
#Depois modifique o programa para que ele mostre os números um ao lado do outro.​

for x in range (20):
    print(x+1)

for y in range (20):
    print(f"{y+1} ", end = "")