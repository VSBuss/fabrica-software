#23 - A granja TecFrango possui um controle automatizado de cada frango da sua produção.
#No pé direito do frango há um anel com um chip de identificação, no pé esquerdo são dois anéis para indicar o tipo de alimento que ele deve consumir.
#Sabendo que o anel com chip custa R$ 4,00 e o anel de alimento custa R$ 3,50.
#Faça um algoritmo para calcular o gasto total da granja (com base na quantidade de frangos digitada pelo usuário) para marcar todos os seus frangos.

frangos = int(input("Digite o total de frangos: "))
# 11 = 3,5*2 + 4
print(f"Você deverá gastar R${frangos*11:.2f}")
