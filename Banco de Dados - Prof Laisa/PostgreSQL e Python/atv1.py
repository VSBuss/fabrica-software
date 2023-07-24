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

##Segundo passo: Atribuir em uma variável a string de conexão
engine = create_engine("postgresql://postgres:1234@localhost:5432/Estudo de Caso 22/05")

##Terceiro passo: Criar a conexão com o PgAdmin
connection = pg.connect(user = "postgres", password = "1234", host = "localhost", port = "5432", database = "Estudo de Caso 22/05")
curs = connection.cursor()

##Quarto passo: Atribuir os comandos:
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
'sql_insert', 'sql_update' e 'sql_delete' foram variáveis criadas para fazerem uma função específica dentro do Query do PgAdmin 4

Assim como as variáveis engine, connection e curs foram criadas para:
var(engine) = create_engine - identificar qual caminho do banco para fazer a conexão; https://docs.sqlalchemy.org/en/20/core/engines.html
var(connection) = pg.connect - cria a interface no Python com o Postgre SQL realizando uma integração entre ambos; https://www.php.net/manual/pt_BR/function.pg-connect.php
var(curs) = connection.cursor - cria uma estrutura de controle que permite percorrer sobre os registros do banco de dados; https://pt.wikipedia.org/wiki/Cursor_(banco_de_dados)
'''