#45 - Faça um algoritmo que receba o ano de nascimento de uma pessoa e o ano atual.
#Calcule e mostre:
#A idade dessa pessoa em anos;
#A idade dessa pessoa em meses;
#A idade dessa pessoa em dias;
#A idade dessa pessoa em semanas.

ano = int(input("Em que ano você nasceu? "))
anoa = int(input("Qual o ano atual? "))

print(f"Você tem {anoa - ano} anos de idade.")
print(f"Já viveu aproximadamente {(anoa - ano)*12} meses.")
print(f"Mais ou menos uns {(anoa-ano)*365} dias.")
print(f"Ou umas {(anoa-ano)*36} semanas.")