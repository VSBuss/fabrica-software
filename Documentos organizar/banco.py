import sqlite3

banco = sqlite3.connect('produtos275.db') #cria uma variável que armazena o banco de dados do   sqlite3 - semelhante a: "CREATE DATABASE produtos275"#
cursor = banco.cursor()

#cursor.execute("CREATE TABLE produtos (id integer primary key autoincrement, nome text not null, qnt integer not null, valor float not null)")#


#CREATE
#cursor.execute("INSERT INTO produtos (nome, qnt, valor) VALUES('Nightbruik', 11, 4206.90)")
#cursor.execute("INSERT INTO produtos (nome, qnt, valor) VALUES('Mouses', 10, 69.69)")
#banco.commit()

#READ
#cursor.execute("SELECT * FROM produtos")
#print(cursor.fetchall())
#banco.commit()

#UPDATE
#cursor.execute("UPDATE produtos SET qnt = 9 WHERE id = 1")
#banco.commit()

#DELETE
#cursor.execute("DELETE FROM produtos WHERE id = 2")
#banco.commit()
