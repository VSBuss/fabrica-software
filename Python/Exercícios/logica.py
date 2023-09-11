try:
    print("RESOLVE O QUEBRA CABEÇA ABAIXO SEGUINDO A SEGUINTE LÓGICA:\n"
          "      ╔═══╗\n"
          "      ║ 9 ║\n"
          "      ╚═══╝\n"
          "   ╔═/═╗ ╔═\═╗\n"
          "   ║ 5 ║+║ 4 ║\n"
          "   ╚═══╝ ╚═══╝\n"
          "Qual o valor do tijolo do topo?\n"
          "               ╔═══╗\n"
          "               ║ ? ║\n"
          "               ╚═══╝\n"
          "            ╔═══╗ ╔═══╗\n"
          "            ║   ║ ║   ║\n"
          "            ╚═══╝ ╚═══╝\n"
          "         ╔═══╗ ╔═══╗ ╔═══╗\n"
          "         ║   ║ ║54 ║ ║   ║\n"
          "         ╚═══╝ ╚═══╝ ╚═══╝\n"
          "      ╔═══╗ ╔═══╗ ╔═══╗ ╔═══╗\n"
          "      ║25 ║ ║   ║ ║32 ║ ║   ║\n"
          "      ╚═══╝ ╚═══╝ ╚═══╝ ╚═══╝\n"
          "   ╔═══╗ ╔═══╗ ╔═══╗ ╔═══╗ ╔═══╗\n"
          "   ║   ║ ║ 7 ║ ║   ║ ║   ║ ║ 3 ║\n"
          "   ╚═══╝ ╚═══╝ ╚═══╝ ╚═══╝ ╚═══╝\n"
          "a) 309\n"
          "b) 205\n"
          "c) 106\n"
          "d) 101\n"
          "e) 207\n")
    alternativa = input()
    alternativa = alternativa.upper()
    if alternativa == 'E' or alternativa == '207':
        print("Ó o cafézin piuí")
    else:
        print("Sem café pra tu maninho.")
except:
    TypeError

'''
conn.execute(INSERT INTO questoes (pergunta, opcao_a, opcao_b, opcao_c, opcao_d, resposta_correta)
    VALUES ('RESOLVE O QUEBRA CABEÇA ABAIXO SEGUINDO A SEGUINTE LÓGICA:\n      ╔═══╗\n      ║ 9 ║
    \n      ╚═══╝\n   ╔═/═╗ ╔═\═╗\n   ║ 5 ║+║ 4 ║\n   ╚═══╝ ╚═══╝\nQual o valor do tijolo do topo?
    \n               ╔═══╗\n               ║ ? ║\n               ╚═══╝\n            ╔═══╗ ╔═══╗
    \n            ║   ║ ║   ║\n            ╚═══╝ ╚═══╝\n         ╔═══╗ ╔═══╗ ╔═══╗\n         ║   ║ ║54 ║ ║   ║
    \n         ╚═══╝ ╚═══╝ ╚═══╝\n      ╔═══╗ ╔═══╗ ╔═══╗ ╔═══╗\n      ║25 ║ ║   ║ ║32 ║ ║   ║
    \n      ╚═══╝ ╚═══╝ ╚═══╝ ╚═══╝\n   ╔═══╗ ╔═══╗ ╔═══╗ ╔═══╗ ╔═══╗\n   ║   ║ ║ 7 ║ ║   ║ ║   ║ ║ 3 ║
    \n   ╚═══╝ ╚═══╝ ╚═══╝ ╚═══╝ ╚═══╝\n"', 'a) 207', 'b) 101', 'c) 106', 'd) 205', 'a')

conn.execute(INSERT INTO questoes (pergunta, opcao_a, opcao_b, opcao_c, opcao_d, resposta_correta)
    VALUES ('Em um prédio com apartamentos somente nos andares de 1° ao 4° moram 4 pessoas
    em andares distintos: Arthur, Leonardo, Marta e Gabriela, não nessa ordem.
    Cada uma dessas pessoas possui ao menos 1 animal de estimação diferente: gato,
    cachorro, passarinho e tartaruga. Gabriela vive reclamando o tempo inteiro do barulho do
    cachorro no andar logo acima do seu. Arthur\nque não mora no 4°, mora um andar acima do de
    Marta.', 'a) Marta não mora no 1° andar.', 'b) Gabriela tem um gato.', 'c) Arthur mora no 3°
    andar e tem um gato.', 'd) Leonardo mora no 4° andar e tem um cachorro.', 'd')

conn.execute(INSERT INTO questoes (pergunta, opcao_a, opcao_b, opcao_c, opcao_d, resposta_correta)
    VALUES ('André acordou atrasado para um compromisso e verificou que o tempo restante
    até o final do dia era igual à metade do tempo já decorrido do dia. Com base nesses dados
    concluímos que ele acordou às:', 'a) 16h', 'b) 12h', 'c) 8h', 'd) 9h', 'a')

conn.execute(INSERT INTO questoes (pergunta, opcao_a, opcao_b, opcao_c, opcao_d, resposta_correta)
    VALUES ('Pedro, Sr. Alcântara, Rafael e Sr. Gonzaga são as 4 primeiras pessoas de uma fila,
    não necessariamente nessa ordem. Teresa Cristina olha para os 4 e afirma: Sr. Alcântara
    e Rafael estão em posições consecutivas na fila e Pedro está entre Sr. Alcântara e
    Rafael. Entretanto Teresa Cristina está mentindo e sabe-se que Sr. Alcântara é o
    terceiro da fila.
    O segundo da fila é: ', 'a) Pedro.', 'b) Sr. Alcântara.', 'c)Rafael.', 'd) Sr. Gonzaga.', 'd')'''