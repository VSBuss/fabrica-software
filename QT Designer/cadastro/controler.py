from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QMessageBox
import pymysql.connections

numero_id = 0

banco = pymysql.connections.Connection(
    host="localhost",
    user="root",
    password="",
    database="cadastro275"
)

# MOSTRA UM POP UP DE ERRO
# https://www.tutorialspoint.com/pyqt/pyqt_qmessagebox.htm
def show_popup():
    msg = QMessageBox()
    msg.setWindowTitle("Erro")
    msg.setText("PREENCHA TODOS OS CAMPOS!")
    msg.setIcon(QMessageBox.Icon.Warning)
    msg.exec()

def popup():
    modalpopup.show()
#Realiza o cadastro
def funcao_principal():
    categoria = ''

    preco = produtos.preco.text()
    codigo = produtos.codigo.text()
    descricao = produtos.descricao.text()

    if produtos.limpeza.isChecked():
        categoria="Limpeza"
    elif produtos.perecivel.isChecked():
        categoria="Perecível"
    elif produtos.bebida.isChecked():
        categoria="Bebidas"

    if codigo == '' or descricao == '' or preco == '' or categoria == '':
        show_popup()
    else:
        #Inserindo dados no banco de dados
        cursor = banco.cursor()
        sql = "INSERT INTO produtos (codigo, descricao, preco, categoria) VALUES (%s,%s,%s,%s)"
        dados = (str(codigo),str(descricao), str(preco), categoria)
        cursor.execute(sql, dados)
        banco.commit()
        produtos.preco.clear()
        produtos.codigo.clear()
        produtos.descricao.clear()

def listar():
    listarProdutos.show()
    
    #Mostrar os dados do banco de dados
    cursor = banco.cursor()
    sql = "SELECT * FROM produtos"
    cursor.execute(sql)
    dados_recebido = cursor.fetchall()

    listarProdutos.tableWidget.setRowCount(len(dados_recebido))
    listarProdutos.tableWidget.setColumnCount(5)

    for linha in range(0,len(dados_recebido)):
        for coluna in range (0,5):
            listarProdutos.tableWidget.setItem(linha,coluna,QtWidgets.QTableWidgetItem(str(dados_recebido[linha][coluna])))

def excluir_dados():
    linha = listarProdutos.tableWidget.currentRow()
    listarProdutos.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute("SELECT id_produtos FROM produtos")
    dados_recebidos = cursor.fetchall()
    valor_id = dados_recebidos[linha][0]
    cursor.execute("DELETE FROM produtos WHERE id_produtos="+str(valor_id))
    banco.commit()

def salvar_dados_editados():
    global numero_id
    print("salvar", numero_id)

    #ler os dados dos lineEdits
    codigo = tela_editar.lineEdit_2.text()
    descricao = tela_editar.lineEdit_3.text()
    preco = tela_editar.lineEdit_4.text()
    categoria = tela_editar.lineEdit_5.text()
    print(codigo, descricao, preco, categoria)

    #atualizar os dados no banco
    cursor = banco.cursor()
    cursor.execute("UPDATE produtos SET codigo = '{}', descricao = '{}', preco = '{}', categoria = '{}' WHERE id_produtos = '{}'".format(codigo, descricao, preco, categoria, numero_id))
    banco.commit()

    #atualizar as janelas
    tela_editar.close()
    listarProdutos.close()
    listar()

def editar_dados():
    global numero_id
    linha = listarProdutos.tableWidget.currentRow()

    cursor = banco.cursor()
    cursor.execute("SELECT id_produtos FROM produtos")
    dados_recebidos = cursor.fetchall()
    valor_id = dados_recebidos[linha][0]
    cursor.execute("SELECT * FROM produtos WHERE id_produtos="+str(valor_id))
    produto = cursor.fetchall()
    tela_editar.show()

    numero_id = valor_id

    tela_editar.lineEdit.setText(str(produto[0][0]))
    tela_editar.lineEdit_2.setText(str(produto[0][1]))
    tela_editar.lineEdit_3.setText(str(produto[0][2]))
    tela_editar.lineEdit_4.setText(str(produto[0][3]))
    tela_editar.lineEdit_5.setText(str(produto[0][4]))

app = QtWidgets.QApplication([])
produtos = uic.loadUi("QT Designer/cadastro/cadastro_produtos.ui")
listarProdutos = uic.loadUi("QT Designer/cadastro/listar_dados.ui")
tela_editar = uic.loadUi("QT Designer/cadastro/modal_editar.ui")
modalpopup = uic.loadUi("QT Designer/cadastro/modal_preencha.ui")
produtos.cadastrar.clicked.connect(funcao_principal)
produtos.listar.clicked.connect(listar)
listarProdutos.deletar.clicked.connect(excluir_dados)
listarProdutos.editar.clicked.connect(editar_dados)
tela_editar.salvar.clicked.connect(salvar_dados_editados)


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
'''