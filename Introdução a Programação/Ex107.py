'''Faça um programa que carregue uma lista com os modelos de cinco carros
(exemplo de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo
desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível.

Calcule e mostre:
O modelo do carro mais econômico;

Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de
1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro.
Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo.
Os dados são fictícios e podem mudar a cada execução do programa.

Comparativo de Consumo de Combustível

Veículo 1
Nome: fusca
Km por litro: 7
Veículo 2
Nome: gol
Km por litro: 10
Veículo 3
Nome: uno
Km por litro: 12.5
Veículo 4
Nome: Vectra
Km por litro: 9
Veículo 5
Nome: Peugeout
Km por litro: 14.5

Relatório Final
1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
2 - gol             -   10.0 -  100.0 litros - R$ 225.00
3 - uno             -   12.5 -   80.0 litros - R$ 180.00
4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17

'''

carlista = ['Fuca', 'Golo', 'Vector', 'Dodgeham', 'Huno']
carsumo = ['14.3', '13.2', '9.5', '8.7', '22.5']

y = carsumo[0]
menor = ''
for x in range(len(carsumo)):
    if y < carsumo[x]:
        menor = carlista[x]
print(f"O carro mais econômico é o carro {menor}.\n\n"
"Comparativo de Consumo de Combustível\n\n")
for x in range(len(carlista)):
    print(f"Veículo {x+1}\nNome: {carlista[x]}\nKm por litro: {carsumo[x]}")
print("\nRelatório Final")
for x in range(len(carlista)):
    y = float(carsumo[x])
    #print(f"{x+1} - {carlista[x]}" + " "*(11-len(carlista[x])), f"{y} -  {1000/y:.2f} litros - R$ {1000/y*2.25:.2f}")
    print(f'{x+1} - {carlista[x]:<11} - {y:^6} - {1000/y:^11.2f} litros - R$ {1000/y*2.25:.2f}')