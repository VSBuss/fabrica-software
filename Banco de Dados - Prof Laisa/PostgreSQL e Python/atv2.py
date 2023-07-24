##Primeiro passo: importar as bibliotecas
import pandas as pd
import psycopg2 as pg
from sqlalchemy import create_engine

'''
Caso não tenha instalado abrir terminal e executar as seguintes linhas:

pip install pandas
pip install psycopg2
pip install sqlalchemy
'''

var = input("Digite um nome para inserir na tabela cliente: ")

##Segundo passo: Atribuir em uma variável a string de conexão
engine = create_engine("postgresql://postgres:1234@localhost:5432/ALUGUEL DE CARRO")

##Terceiro passo: Criar a conexão com o PgAdmin
connection = pg.connect(user = "postgres", password = "1234", host = "localhost", port = "5432", database = "ALUGUEL DE CARRO")
curs = connection.cursor()

##Quarto passo: Atribuir os comandos:
sql_insert = "INSERT INTO cliente (nome) VALUES ('%s')" % var
curs.execute(sql_insert)
connection.commit()

sql_update = "UPDATE cliente SET nome = 'Patrícia' WHERE id_cliente = 4"
curs.execute(sql_update)
connection.commit()

sql = "SELECT id_cliente, nome FROM cliente order by id_cliente"
df = pd.read_sql_query(sql, con=engine)
print(df)

var1 = input("Digite o id da última pessoa que você adicionou: ")

sql_delete = "DELETE FROM cliente WHERE id_cliente = '%s'" % var1
curs.execute(sql_delete)
connection.commit()

df = pd.read_sql_query(sql, con=engine)
print(df)


'''
'sql_insert', 'sql_update' e 'sql_delete' foram variáveis criadas para fazerem uma função específica dentro do Query do PgAdmin 4

Assim como as variáveis engine, connection e curs foram criadas para:
var(engine) = create_engine - identificar qual caminho do banco para fazer a conexão; https://docs.sqlalchemy.org/en/20/core/engines.html
var(connection) = pg.connect - cria a interface no Python com o Postgre SQL realizando uma integração entre ambos; https://www.php.net/manual/pt_BR/function.pg-connect.php
var(curs) = connection.cursor - cria uma estrutura de controle que permite percorrer sobre os registros do banco de dados; https://pt.wikipedia.org/wiki/Cursor_(banco_de_dados)
'''