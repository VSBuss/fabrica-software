#37 - A padaria Super Pão vende uma certa quantidade de pães franceses e uma quantidade de broas a cada dia.
#Cada pãozinho custa R$ 1,00 e a broa custa R$ 3,50.
#Ao final do dia, o dono quer saber quanto arrecadou com a venda dos pães e broas (juntos), e quanto deve guardar numa conta de poupança (10% do total arrecadado).
#Você foi contratado para fazer os cálculos para o dono.
#Com base nestes fatos, faça um algoritmo para ler as quantidades de pães e de broas, e depois calcular os dados solicitados. ​

pao = int(input("Digite a quantidade de pães vendidos: "))
broa = int(input("Digite a quantidade de broas vendidas: "))
totalvenda = pao + broa * 3.5
print(f"O total arrecadado foi de R${totalvenda} e o total a ser guardado na poupança é de R${totalvenda*0.1}.")