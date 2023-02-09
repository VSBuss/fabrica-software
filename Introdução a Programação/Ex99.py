'''
Fatura da Águas Guariroba – as regras que a Águas Guariroba utiliza para cobrar a fatura de água e esgoto
de clientes residenciais estão expressas na tabela abaixo. Repare que existem 6 faixas de consumo e que
cada uma possui uma franquia de consumo e um valor diferente para cada metro cúbico (m3) consumido.

                FAIXAS DE CONSUMO                    |  TOTAIS(R$)    |
faixa | Volume da faixa |Franquia de Consumo | Valor |  Água | Esgoto |
  1°  | Mínimo (até 5m³)|        5m³         |R$37,47| 37,47 |  29,97 |
  2°  |  de 6m³ a 10m³  |        5m³         | R$1,16|  5,80 |   4,64 |
  3°  | de 11m³ a 15m³  |        5m³         | R$6,46| 32,30 |  25,84 |
  4°  | de 16m³ a 20m³  |        5m³         | R$6,49| 32,45 |  25,96 |
  5°  | de 21m³ a 30m³  |       10m³         | R$6,55| 65,50 |  52,40 |
  6°  |  acima de 30m³  |       Livre        |R$11,08|       |        |

O valor de uma fatura é calculado distribuindo-se o consumo total de água de água pelas faixas de consumo.
Caso um cliente tenha consumido menos de 5 m3, deve pagar a tarifa mínima (R$ 37,47) mas se consumiu digamos,
12 m3 de água, 5m3 são cobrados pela 1ª faixa, outros 5m3 pela 2ª faixa e os 2m3 restantes são cobrados pela 3ª faixa.
O valor do esgoto é calculado como sendo 80% do valor cobrado pela água. A coluna “Totais” mostra quanto seria
cobrado de um cliente que tenha consumido toda a franquia das faixas correspondentes (com exceção da última faixa, que não possui franquia de consumo).

Com base nessas informações, elabore um programa que calcule o valor da fatura de um cliente
com base em seu consumo de água, utilizando o exemplo a seguir para auxiliar na compreensão do problema.

Exemplo: Assuma que que um determinado domicílio consumiu 37 m3 de água num determinado mês.
Para o cálculo da respectiva fatura, deve-se distribuir esse volume pelas faixas de consumo da tabela, como explicado abaixo:

(1) 1ª faixa (franquia de 5 m³) – O consumo dos primeiros 5(cinco) m³ de água são faturados pela tarifa mínima,
que é de R$ 37,47. Dos 37 m³ consumidos, restam 32 m³ para serem faturados pelas demais faixas de consumo;

(2) 2ª faixa (franquia de 5 m³) – Os próximos5 (cinco) m³ que ultrapassam o consumo da 1ª faixa são cobrados pelo
valor de excedente da2ª faixa de consumo da tabela abaixo (5m³ x R$ 1,16 = R$ 5,80). Dos 37 m³ consumidos,
5 foram faturados pela 1ª faixa e outros 5 pela 2ª faixa restando, portanto, 27 m³ para serem faturados;

(3) 3ª faixa (franquia de 5 m³) – Os próximos 5 (cinco) m³ que ultrapassam o consumo da 2ª faixa são cobrados pelo
valor de excedente da 3ª faixa de consumo (5 m³ x R$ 6,46 = R$ 32,30). Até essa faixa, foram faturados 15 m³ e restam ainda 22 m³ para serem faturados;

(4) 4ª faixa (franquia de 5 m³) – Os próximos 5 (cinco) m³ que ultrapassam o consumo da 3ª faixa são cobrados pelo
valor de excedente da 4ª faixa de consumo (5 m³ x R$ 6,49 = R$ 32,45). Até essa faixa, foram faturados 20 m³ e restam ainda 17 m³ para serem faturados;

(5) 5ª faixa (franquia de 10 m³) – Os próximos 10 (dez) m³ que ultrapassam o consumo da 4ª faixa são cobrados pelo
valor de excedente da 5ª faixa de consumo (10 m³ x R$ 6,55 = R$ 65,50). Até essa faixa, foram faturados 30 m³ e restam ainda 7 m³ para serem faturados;

(6)6ª faixa (franquia livre) – Os próximos 7 (sete) m³ que ultrapassam o consumo da 5ª faixa são cobrados pelo
valor de excedente da 6ª faixa de consumo (7 m³ x R$ 11,08 = R$ 77,56). Até essa faixa, foram faturados 37 m³, que foi o valor consumido pelo cliente;

(7) Para obter o valor da água consumida, deve-se somar o consumo em cada faixa, ou seja,
R$ 37,47 + R$ 5,80 + R$ 32,30 + R$ 32,45 + R$ 65,50 + R$ 77,56 = R$ 251, 08;

(8) O valor referente ao esgoto corresponde a 80% do valor da água, ou seja, R$ 251,08 x 0,8 = R$ 200,86;

(9) O valor da fatura é dado pela soma do consumo de água pela do esgoto, ou seja, R$ 251,08 + R$ 200,86 = R$ 451,94.

'''

consumo = int(input("Informe qual foi o consumo de água em m³: "))
consumo2 = consumo
total = 0
while consumo > 30:
  total = total + 11.08
  consumo -= 1
while  20 < consumo <= 30:
  total = total + 6.55
  consumo -= 1
while 15 < consumo <= 20:
  total = total + 6.49
  consumo -= 1
while 10 < consumo <= 15:
  total = total + 6.46
  consumo -= 1
while 5 < consumo <= 10:
  total = total + 1.16
  consumo -= 1
if consumo <= 5:
  total = total + 37.47

print(f"O consumo de {consumo2}m³ de água gerou uma fatura no valor de:\nR${total:.2f} referente à água.\n"
f"R${total*0.8:.2f} referente ao esgoto.\nTotalizando R${total+total*0.8:.2f}.")