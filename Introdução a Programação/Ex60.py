#Faça um algoritmo que leia um valor correspondente ao número de jogadores de um time de basquete.
#O programa deverá ler uma altura para cada um dos jogadores e, ao final, informar a altura média do time usando FOR.

totalj = int(input("Quantos jogadores há no time de basquete? "))
htotal = 0
for x in range(totalj):
    altura = int(input(f"Informe a altura em centímetros do jogador {x+1}: "))
    htotal = htotal + altura
print(f"A altura média do time é de {htotal/totalj}cm.")