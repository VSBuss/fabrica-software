'''Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados
quando for informado um valor igual a -1 (que não deve ser armazenado).
Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;'''
qnt = acima = abaixo = 0
notas = []
print("Insira várias notas. Caso queira parar insira o valor '-1' para encerrar a entrada de dados:")
while True:
    valor = float(input())
    if valor == -1:
        break
    notas.append(valor)
    qnt += 1
print(f"\nQuantidade de notas inseridas: {qnt}\nNotas: {notas}\nOrdem inversa: ")
for x in range(qnt):
    if notas[x] > sum(notas)/qnt:
        acima += 1
    if notas[x] < 7:
        abaixo += 1
    print(notas[- 1 + x*-1])
print(f"Soma: {sum(notas)}\nMédia: {sum(notas)/qnt:.2f}\nQuantidade de notas acima da média total: {acima}\nQuantidade de notas abaixo de 7: {abaixo}")
print("Fim do programa")