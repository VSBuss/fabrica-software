from PyQt6 import uic, QtWidgets
import pymysql.connections

banco = pymysql.connections.Connection(
    host = "localhost",
    user = "root",
    password = "",
    database = "NomeDoBancoDeDados"
)

def funcao_principal():
    codigo = produtos.codigo.text()
    descricao = produtos.descricao.text()
    preco = produtos.preco.text()
    print("Código: ", codigo)
    print("Nome: ", descricao)
    print("Valor: ", preco)

    if produtos.limpeza.isChecked():
        print("Categoria Limpeza")
        categoria = 'Limpeza'
    elif produtos.bebidas.isChecked():
        print("Categoria Bebidas")
        categoria = 'Bebidas'
    elif produtos.perecivel.isChecked():
        print("Categoria Perecivel")
        categoria = 'Perecível'

    #Inserindo dados no banco de dados
    cursor = banco.cursor()
    sql = "INSERT INTO produtos (codigo, descricao, preco, categoria) VALUES (%s, %s, %s, %s)"
    dados = (str(codigo), str(descricao), str(preco), str(categoria))
    cursor.execute(sql, dados)
    banco.commit()

def listar():
    listaDeProdutos.show()
    
    #Mostrar os dados do banco de dados
    cursor = banco.cursor()
    sql = "SELECT * FROM produtos"
    cursor.execute(sql)
    dados_recebidos = cursor.fetchall()
    
    listaDeProdutos.tableWidget.setRowCount(len(dados_recebidos))
    listaDeProdutos.tableWidget.setColumnCount(len(dados_recebidos))

    for linha in range(0, len(dados_recebidos)):
        for coluna in range (0,5):
            listaDeProdutos.tableWidget.setItem(QTableWidgetItem(str(dados_recebidos[linha][coluna])))


app = QtWidgets.QApplication([])
produtos = uic.loadUi('cadastroprodutos.ui')
listaDeProdutos = uic.loadUi("listadeprodutos.ui")
produtos.cadastrar.clicked.connect(funcao_principal)
produtos.listar.clicked.connect(listar)
produtos.show()
app.exec()

'''
Criar telas no QTDesigner
Instalar: pip install mysql-connector-python
pip install PyMySQL


Acessar no browser: //localhost/phpmyadmin

Criar banco de dados para realizar o exercício

CREATE TABLE produtos(
    id_produtos INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    codigo INT,
    descricao VARCHAR(50),
    preco DOUBLE,
    categoria VARCHAR(30)
);

CREATE TABLE carros(
    id_carros INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    
)
'''