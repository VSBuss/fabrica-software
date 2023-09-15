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

from classes import Conta
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

## EXEMPLOS ^^^^^^^^^^

## INSERE OS VALORES DOS NOMES DE TIPO E GRUPO DO BANCO DE DADOS NAS VARIÁVEIS DO TIPO LISTA COM O NOME DE tipo e grupo
tipo = []
grupo = []

x = 0
sql = "SELECT nome FROM tipo"
df = pd.read_sql_query(sql, con=engine)
while x < df.shape[0]:
    variable = df['nome'].values[x]
    tipo.append(variable)
    x = x + 1

x = 0
sql = "SELECT nome FROM grupo"
df = pd.read_sql_query(sql, con=engine)
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
    if opcoes == '1':
        opcoes2 = input("\n----------DIANE----------\n\n"
                            "[1] - Cadastrar Conta\n"
                            "[2] - Investimento\n"
                            "[3] - Mostrar Relatório\n"
                            "[4] - Voltar\n\n")
        if opcoes2 == '1':
            receita_despesa = int(input("\nQue tipo de conta deseja cadastrar?\n"
                                    "[1] - Receita\n"
                                    "[2] - Despesa\n\n"))
            print("\nComplete os campos abaixo:\n")
            for indice, contador in enumerate(tipo):
                print(f"[{indice}] - {contador}")
            descricao = input("Descrição: ")
            grupo = 1
            valor = float(input("Valor: "))
            data_cadastro = date.today()
            data_cadastro = data_cadastro.strftime("%d/%m/%Y")
            data_vencimento = input("Data de vencimento [dd/mm/ano]: ")
            situacao = input("A conta está paga?\n[1] - SIM\n[2] - NÃO\n")
            conta = Conta(receita_despesa, descricao, tipo, grupo, valor, data_cadastro, data_vencimento, situacao)
            conta.cadastrarConta()
            contas.append(conta)
        elif opcoes2 == '2':
            a=a
        elif opcoes2 == '3':
            a=a
        elif opcoes2 == '4':
            a=a
        else:
            print("\nEntrada Inválida")
        
    elif opcoes == '2':
        operacoes = input("\n----DIANE----\n"
                        "----Conta Pessoal----\n"
                            "1-Boletos\n"
                            "2-Relatórios\n"
                            "3-Saldo\n"
                            "4-Sair\n")
    elif opcoes == '3':
        print("\nTchau =)")
    else:
        print("\nEntrada Inválida")