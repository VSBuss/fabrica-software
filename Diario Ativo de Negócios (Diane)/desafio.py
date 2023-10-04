## Importar as bibliotecas
import pandas as pd
import psycopg2 as pg
from sqlalchemy import create_engine

'''
Caso não tenha instalado abrir terminal e executar as seguintes linhas:

pip install pandas
pip install psycopg2
pip install sqlalchemy
'''

from datetime import date

## Variável da string de conexão
engine = create_engine("postgresql://postgres:1234@localhost:5432/DIANE")

## Criar a conexão com o PgAdmin
connection = pg.connect(user = "postgres", password = "1234", host = "localhost", port = "5432", database = "DIANE")
curs = connection.cursor()

##Quarto passo: Atribuir os comandos:
'''
sql_insert = "INSERT INTO cliente (nome, cpf_cliente, email, country) VALUES ('Pedro de Alcântara João Carlos Leopoldo Salvador Bibiano Francisco Xavier de Paula Leocádio Miguel Gabriel Rafael Gonzaga', '765.237.468-00', 'pedroajclsbfxplmgrg@imperio.com.br', 'Brasil')"
curs.execute(sql_insert)
connection.commit()

sql_update = "UPDATE cliente SET nome = 'Maria das Dores' WHERE id_cliente = 4"
curs.execute(sql_update)
connection.commit()

sql_delete = "DELETE FROM cliente WHERE id_cliente in (10, 11, 12, 13)"
curs.execute(sql_delete)
connection.commit()

sql = "SELECT nome, email FROM cliente"
df = pd.read_sql_query(sql, con=engine)
print(df)
'''

## Comandos para criação do BD:
'''
CREATE TABLE tipo(
	id_tipo int PRIMARY KEY,
	nome VARCHAR
);
CREATE TABLE grupo(
	id_grupo int PRIMARY KEY,
	nome VARCHAR
);
CREATE TABLE conta(
	id int PRIMARY KEY,
	receita_despesa BOOL,
	valor FLOAT NOT NULL,
	data_cadastro DATE NOT NULL,
	data_vencimento DATE NOT NULL,
	data_pg DATE,
	situacao BOOL,
	id_tipo INT NOT NULL,
	id_grupo INT NOT NULL,
	FOREIGN KEY (id_tipo) REFERENCES tipo (id_tipo),
	FOREIGN KEY (id_grupo) REFERENCES grupo (id_grupo)
);
CREATE TABLE saldo(
    valor float
);
'''

## EXEMPLOS ^^^^^^^^^^

## INSERE OS VALORES DOS NOMES DE TIPO E GRUPO DO BANCO DE DADOS NAS VARIÁVEIS DO TIPO LISTA COM O NOME DE tipo e grupo
tipo = []
grupo = []

## Seleciona e insere os nomes dos grupos e tipos de conta nas listas acima.
sql = "SELECT nome FROM tipo"
df = pd.read_sql_query(sql, con=engine)
x = 0
while x < df.shape[0]:
    variable = df['nome'].values[x]
    tipo.append(variable)
    x = x + 1

sql = "SELECT nome FROM grupo"
df = pd.read_sql_query(sql, con=engine)
x = 0
while x < df.shape[0]:
    variable = df['nome'].values[x]
    grupo.append(variable)
    x = x + 1

## Cria as contas:
contas = []

opcoes = 0
while opcoes != '3':
    opcoes = input("\n----------DIANE----------\n"
                   "[1] - Contas\n"
                   "[2] - Relatórios\n"
                   "[3] - Sair\n\n")
    if opcoes == '1': ## Contas
        opcoes2 = input("\n----------DIANE----------\n\n"
                        "[1] - Cadastrar Conta\n"
                        "[2] - Sugestões de Investimento\n"
                        "[3] - Voltar\n\n")
        if opcoes2 == '1':
            receita_despesa = input("\nQue tipo de conta deseja cadastrar?\n"
                                        "[1] - Despesa\n"
                                        "[0] - Receita\n\n")
            print("\nComplete os campos abaixo:\n")
            for indice, contador in enumerate(tipo):
                print(f"[{indice}] - {contador}")
            descricao = int(input("Descrição: "))
            grupo = 1
            valor = float(input("Valor: "))
            data_cadastro = date.today()
            data_cadastro = data_cadastro.strftime("%d/%m/%Y")
            data_vencimento = input("Data de vencimento [dd/mm/ano]: ")
            while True:
                situacao = input("A conta está paga?\n[1] - SIM\n[0] - NÃO\n")
                if situacao == '1':
                    # Executar uma instrução SQL para inserir dados em uma tabela
                    curs.execute("INSERT INTO conta (receita_despesa, valor, data_cadastro, data_vencimento, data_pg, situacao, id_tipo, id_grupo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                                (receita_despesa, valor, data_cadastro, data_vencimento, data_cadastro, situacao, descricao, grupo))
                    # Confirmar a transação
                    connection.commit()
                    # Fechar a conexão
                    connection.close()
                    break
                elif situacao == '0':
                    # Executar uma instrução SQL para inserir dados em uma tabela
                    curs.execute("INSERT INTO conta (receita_despesa, valor, data_cadastro, data_vencimento, situacao, id_tipo, id_grupo) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                                (receita_despesa, valor, data_cadastro, data_vencimento, situacao, descricao, grupo))
                    # Confirmar a transação
                    connection.commit()
                    # Fechar a conexão
                    connection.close()
                    break
                else:
                    print("\nEntrada Inválida.")
                    continue

        elif opcoes2 == '2':
            1==1
        elif opcoes2 == '3':
            print("\n"*6)
        else:
            print("\nEntrada Inválida")
        
    elif opcoes == '2': ## Relatórios
        opcoes3 = input("\n----------DIANE----------\n"
                          "------Conta Pessoal------\n"
                          "[1] - Despesas Pagas\n"
                          "[2] - Despesas em Aberto\n"
                          "[3] - Receitas Recebidas\n"
                          "[4] - Receitas a Receber\n"
                          "[5] - Relatório Geral\n"
                          "[6] - Saldo\n"
                          "[7] - Voltar\n\n")
        ## DESPESAS PAGAS
        if opcoes3 == '1':
            print("\nInforme o intervalo de tempo para gerar o relatório:")
            datainicial = input("Data Inicial: ")
            datafinal = input("Data Final: ")
            print("\n")
            sql =  "SELECT valor, grupo.nome as nomegrupo, tipo.nome FROM conta " \
                   "JOIN grupo " \
                   "ON conta.id_grupo = grupo.id_grupo " \
                   "JOIN tipo " \
                   "ON conta.id_tipo = tipo.id_tipo " \
                   "WHERE data_pg IS NOT NULL"
            df = pd.read_sql_query(sql, con=engine)
            x=0
            while x < df.shape[0]:
                valor = df['valor'].values[x]
                nomegrupo = df['nomegrupo'].values[x]
                nomeconta = df['nome'].values[x]
                print(f"R${valor:.2f} - {nomeconta}")
                x = x + 1

        ## DESPESAS EM ABERTO
        elif opcoes3 == '2':
            sql = "SELECT * FROM conta" \
            "JOIN grupo" \
            "ON conta.id_grupo = grupo.id_grupo" \
            " WHERE data_pg IS NULL"
            df = pd.read_sql_query(sql, con=engine)
            print(df)
            x = 0
            while x < df.shape[0]:
                nome = df['nome'].values[x]
                x = x + 1
                print(nome)

        ## RECEITAS RECEBIDAS
        elif opcoes3 == '3':
            1==1

        ## RECEITAS A RECEBER
        elif opcoes3 == '4':
            1==1

        ## RELATÓRIO GERAL
        elif opcoes3 == '5':
            1==1

        ## SALDO
        elif opcoes3 == '6': 
            sql = "SELECT * FROM saldo"
            df = pd.read_sql_query(sql, con=engine)
            saldo = df['valor'].values[0]
            saldo = float(saldo)
            print(f"\nSALDO ATUAL: R$ {saldo:.2f}")

        ## VOLTAR
        elif opcoes3 == '7':
            print("\n"*6)
        
        ## EXCEPTION
        else:
            print("\nEntrada Inválida")
        
    elif opcoes == '3': ## Sair
        print("\nTchau =)")
    else:
        print("\nEntrada Inválida")

## Tratamento de exceções e calcular e inserir juros
