from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QMessageBox
import pymysql.connections

numero_id = 0

banco = pymysql.connections.Connection(
    host="localhost",
    user="root",
    password="",
    database="hellomoto"
)

# MOSTRA UM POP UP DE ERRO
# https://www.tutorialspoint.com/pyqt/pyqt_qmessagebox.htm

def show_popup():
    msg = QMessageBox()
    msg.setWindowTitle("Erro")
    msg.setText("PREENCHA TODOS OS CAMPOS!")
    msg.setIcon(QMessageBox.Icon.Warning)
    msg.exec()

#Realiza a compra
def tela_comprar():
    #Usar categoria para definir a compra
    if telamain.alugueld.isChecked():
        categoria="diario"
    elif telamain.aluguelm.isChecked():
        categoria="mensal"
    elif telamain.compra.isChecked():
        categoria="compra"
    
    ##Os dois abaixo não podem ser QLineEdit
    ##total de dias deve ser colocado na label
    ##valor deve ser considerado de acordo com a db

    if telamain.checkPix.isChecked():
        a = a
    elif telamain.checkTED.isChecked():
        a = a


#Realiza o cadastro
def funcao_cadastrar():

    codigo = cadastromotos.codigo.text()
    descricao = cadastromotos.descricao.text()
    precodiaria = cadastromotos.preco_dia.text()
    precomensal = cadastromotos.preco_mes.text()
    precovenda = cadastromotos.preco_venda.text()

    if codigo == '' or descricao == '' or precodiaria == '' or precomensal == '' or precovenda == '':
        show_popup()
    else:
        #Inserindo dados no banco de dados
        cursor = banco.cursor()
        sql = "INSERT INTO motos (codigo, descricao, precodiaria, precomensal, precovenda) VALUES (%s,%s,%s,%s,%s)"
        dados = (str(codigo),str(descricao), str(precodiaria), str(precomensal), str(precovenda))
        cursor.execute(sql, dados)
        banco.commit()
        cadastromotos.preco.clear()
        cadastromotos.codigo.clear()
        cadastromotos.descricao.clear()

def listar():
    listaprod.show()
    
    #Mostrar os dados do banco de dados
    cursor = banco.cursor()
    sql = "SELECT * FROM motos"
    cursor.execute(sql)
    dados_recebido = cursor.fetchall()

    listaprod.tableWidget.setRowCount(len(dados_recebido))
    #Usar 6 por causa da quantidade de colunas (id, código, descrição, preço diária, preço mensal e preço venda)
    listaprod.tableWidget.setColumnCount(6)

    for linha in range(0,len(dados_recebido)):
        for coluna in range (0,6):
            listaprod.tableWidget.setItem(linha,coluna,QtWidgets.QTableWidgetItem(str(dados_recebido[linha][coluna])))

def excluir_dados():
    linha = listaprod.tableWidget.currentRow()
    listaprod.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute("SELECT id_produtos FROM produtos")
    dados_recebidos = cursor.fetchall()
    valor_id = dados_recebidos[linha][0]
    cursor.execute("DELETE FROM motos WHERE id_produtos="+str(valor_id))
    banco.commit()

def salvar_dados_editados():
    global numero_id

    #ler os dados dos lineEdits
    codigo = telaeditar.ln_cod.text()
    descricao = telaeditar.ln_desc.text()
    precodiaria = telaeditar.ln_dia.text()
    precomensal = telaeditar.ln_mes.text()
    precovenda = telaeditar.ln_venda.text()

    #atualizar os dados no banco
    cursor = banco.cursor()
    cursor.execute("UPDATE motos SET codigo = '{}', descricao = '{}', precodiaria = '{}', precomensal = '{}', precovenda = '{}' WHERE id_produtos = '{}'".format(codigo, descricao, precodiaria, precomensal, precovenda, numero_id))
    banco.commit()

    #atualizar as janelas
    telaeditar.close()
    listaprod.close()
    listar()

def editar_dados():
    global numero_id
    linha = listaprod.tableWidget.currentRow()

    cursor = banco.cursor()
    cursor.execute("SELECT id_produtos FROM motos")
    dados_recebidos = cursor.fetchall()
    valor_id = dados_recebidos[linha][0]
    cursor.execute("SELECT * FROM motos WHERE id_produtos="+str(valor_id))
    produto = cursor.fetchall()
    telaeditar.show()

    numero_id = valor_id

    telaeditar.ln_cod.setText(str(produto[0][0]))
    telaeditar.ln_desc.setText(str(produto[0][1]))
    telaeditar.ln_dia.setText(str(produto[0][2]))
    telaeditar.ln_mes.setText(str(produto[0][3]))
    telaeditar.ln_venda.setText(str(produto[0][4]))

app = QtWidgets.QApplication([])

#Conexões de telas

##TELAS
telamotos = uic.loadUi(r'D:\fabrica-software\QT Designer\Hello Moto\motos.ui')
telaeditar = uic.loadUi(r'D:\fabrica-software\QT Designer\Hello Moto\editar.ui')
telamain = uic.loadUi(r'D:\fabrica-software\QT Designer\Hello Moto\hello_moto.ui')
listaprod = uic.loadUi(r'D:\fabrica-software\QT Designer\Hello Moto\lista_prod.ui')
cadastromotos = uic.loadUi(r'D:\fabrica-software\QT Designer\Hello Moto\cadastro_motos.ui')

cadastromotos.listar.clicked.connect(listaprod)
cadastromotos.cadastrar.clicked.connect(funcao_cadastrar)
telaeditar.salvar.clicked.connect(salvar_dados_editados)
listaprod.deletar.clicked.connect(excluir_dados)
cadastromotos.listar.clicked.connect(listar)
listaprod.editar.clicked.connect(editar_dados)

##Ideia de talvez usar 
telamotos.btn_bmw_r1250.clicked.connect()
telamotos.btn_bmw_r18.clicked.connect()
telamotos.btn_hd_glide.clicked.connect()
telamotos.btn_honda.clicked.connect()
telamotos.btn_triumph_100.clicked.connect()
telamotos.btn_triumph_900.clicked.connect()






telamain.show()
app.exec()

'''
Criar telas no QTDesigner
Instalar: pip install mysql-connector-python
pip install PyMySQL


Acessar no browser: //localhost/phpmyadmin

Criar banco de dados para realizar o exercício

CREATE TABLE motos(
    id_produtos INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    codigo INT,
    descricao VARCHAR(50),
    precodiaria DOUBLE,
    precomensal DOUBLE,
    precovenda DOUBLE
);


Abrir pasta onde estão os arquivos, trocar o caminho por 'cmd' dar enter e executar o seguinte comando de acordo com o nome dos arquivos ui para trocá-los por py
python -m PyQt6.uic.pyuic -o output.py -x input.ui
'''