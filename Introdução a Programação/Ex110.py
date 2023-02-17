'''Faça um programa que simule um lançamento de dados.
Lance o dado 100 vezes e armazene os resultados em um vetor.
Depois, mostre quantas vezes cada valor foi conseguido.
Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.'''
import random
numeros = [0, 0, 0, 0, 0, 0]
for x in range(100):
    num = random.randint(1,6)
    numeros[num-1] += 1
print(numeros)