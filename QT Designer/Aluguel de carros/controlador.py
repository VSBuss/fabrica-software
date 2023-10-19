from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QMessageBox
import pymysql

numero_id = 0
cpfcliente = ''
placacarro = ''
categoria = ''

banco = pymysql.connect(
    host='localhost',
    user='root',
    password="",
    db='aluguelcarros'
)

# if produtos.limpeza.isChecked():
#     categoria="Limpeza"
# elif produtos.perecivel.isChecked():
#     categoria="Perecível"
# elif produtos.bebida.isChecked():
#     categoria="Bebidas"

# MOSTRA UM POP UP DE ERRO
# https://www.tutorialspoint.com/pyqt/pyqt_qmessagebox.htm
def abrir_cadastro_carros():
    cadastrocarros.show()
def abrir_cadastro_clientes():
    cadastrousuarios.show()
def abrir_tela_venda():
    telavenda.show()
def show_popup():
    msg = QMessageBox()
    msg.setWindowTitle("Erro")
    msg.setText("PREENCHA TODOS OS CAMPOS!")
    msg.setIcon(QMessageBox.Icon.Warning)
    msg.exec()
def venda_popup():
    msg = QMessageBox()
    msg.setWindowTitle("Erro")
    msg.setText("CPF OU PLACA INCORRETAS")
    msg.setIcon(QMessageBox.Icon.Warning)
    msg.exec()
#Realiza o cadastro dos carros
def cadastro_carro():
    marca = cadastrocarros.marca.text()
    descricao = cadastrocarros.descricao.text()
    placa = cadastrocarros.placa.text()
    preco_diaria = cadastrocarros.preco_diaria.text()
    preco_mensal = cadastrocarros.preco_mensal.text()
    preco_venda = cadastrocarros.preco_venda.text()


    if marca == '' or descricao == '' or placa == '' or preco_diaria == '' or preco_mensal == '' or preco_venda == '':
        show_popup()
    else:
        #Inserindo dados no banco de dados
        cursor = banco.cursor()
        sql = "INSERT INTO carro (marca, descricao, placa, precodiaria, precomensal ,precovenda) VALUES (%s,%s,%s,%s,%s,%s)"
        dados = (str(marca),str(descricao), str(placa), preco_diaria, preco_mensal, preco_venda)
        cursor.execute(sql, dados)
        banco.commit()
        cadastrocarros.close()
        telaprincipal.show()
#Realiza o cadastro dos clientes
def cadastro_cliente():
    nome = cadastrousuarios.nome.text()
    rg = cadastrousuarios.rg.text()
    cpf = cadastrousuarios.cpf.text()
    email = cadastrousuarios.email.text()
    telefone = cadastrousuarios.telefone.text()
    endereco = cadastrousuarios.endereco.text()
    cep = cadastrousuarios.cep.text()


    if nome == '' or rg == '' or cpf == '' or email == '' or telefone == '' or endereco == '' or cep == '':
        show_popup()
    else:
        #Inserindo dados no banco de dados
        cursor = banco.cursor()
        sql = "INSERT INTO cliente (nome, rg, cpf, email, telefone, endereco, cep) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        dados = (str(nome),str(rg), str(cpf), str(email), str(telefone), str(endereco), str(cep))
        cursor.execute(sql, dados)
        banco.commit()
        cadastrousuarios.close()
        telaprincipal.show()
#Lista os carros
def listar_carros():
    listarcarros.show()
    
    #Mostrar os dados do banco de dados
    cursor = banco.cursor()
    sql = "SELECT * FROM carro"
    cursor.execute(sql)
    dados_recebidos = cursor.fetchall()

    listarcarros.tableWidget.setRowCount(len(dados_recebidos))
    listarcarros.tableWidget.setColumnCount(5)

    for linha in range(0,len(dados_recebidos)):
        for coluna in range (0,7):
            listarcarros.tableWidget.setItem(linha,coluna,QtWidgets.QTableWidgetItem(str(dados_recebidos[linha][coluna])))
#Lista os clientes
def listar_clientes():
    listarclientes.show()
    
    #Mostrar os dados do banco de dados
    cursor = banco.cursor()
    sql = "SELECT * FROM cliente"
    cursor.execute(sql)
    dados_recebidos = cursor.fetchall()

    listarclientes.tableWidget.setRowCount(len(dados_recebidos))
    listarclientes.tableWidget.setColumnCount(5)

    for linha in range(0,len(dados_recebidos)):
        for coluna in range (0,8):
            listarclientes.tableWidget.setItem(linha,coluna,QtWidgets.QTableWidgetItem(str(dados_recebidos[linha][coluna])))
#Exclui o carro selecionado
def excluir_carro():
    linha = listarcarros.tableWidget.currentRow()
    listarcarros.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute("SELECT id_carro FROM carro")
    dados_recebidos = cursor.fetchall()
    valor_id = dados_recebidos[linha][0]
    cursor.execute("DELETE FROM carro WHERE id_carro="+str(valor_id))
    banco.commit()
#Salva o carro editado
def salvar_carro_editado():
    global numero_id

    #ler os dados dos lineEdits
    marca = editarcarro.marca.text()
    descricao = editarcarro.descricao.text()
    placa = editarcarro.placa.text()
    precodiaria = editarcarro.precodiaria.text()
    precomensal = editarcarro.precomensal.text()
    precovenda = editarcarro.precovenda.text()

    #atualizar os dados no banco
    cursor = banco.cursor()
    cursor.execute("UPDATE carro SET marca = '{}', descricao = '{}', placa = '{}', precodiaria = '{}', precomensal = '{}', precovenda = '{}' WHERE id_carro = '{}'".format(marca, descricao, placa, precodiaria, precomensal, precovenda, numero_id))
    banco.commit()

    #atualizar as janelas
    editarcarro.close()
    listarcarros.close()
    listar_carros()
#Salva o cliente editado
def salvar_cliente_editado():
    global numero_id

    #ler os dados dos lineEdits
    nome = editarcliente.nome.text()
    rg = editarcliente.rg.text()
    cpf = editarcliente.cpf.text()
    email = editarcliente.email.text()
    telefone = editarcliente.telefone.text()
    endereco = editarcliente.endereco.text()
    cep = editarcliente.cep.text()

    #atualizar os dados no banco
    cursor = banco.cursor()
    cursor.execute("UPDATE cliente SET nome = '{}', rg = '{}', cpf = '{}', email = '{}',  telefone = '{}', endereco = '{}', cep = '{}' WHERE id_cliente = '{}'".format(nome, rg, cpf, email, telefone, endereco, cep, numero_id))
    banco.commit()

    #atualizar as janelas
    editarcliente.close()
    listarclientes.close()
    listar_clientes()
#Edita o carro selecionado
def editar_carro():
    global numero_id
    linha = listarcarros.tableWidget.currentRow()

    cursor = banco.cursor()
    cursor.execute("SELECT id_carro FROM carro")
    dados_recebidos = cursor.fetchall()
    valor_id = dados_recebidos[linha][0]
    cursor.execute("SELECT * FROM carro WHERE id_carro="+str(valor_id))
    carro = cursor.fetchall()
    editarcarro.show()

    numero_id = valor_id

    editarcarro.marca.setText(str(carro[0][1]))
    editarcarro.descricao.setText(str(carro[0][2]))
    editarcarro.placa.setText(str(carro[0][3]))
    editarcarro.precodiaria.setText(str(carro[0][4]))
    editarcarro.precomensal.setText(str(carro[0][5]))
    editarcarro.precovenda.setText(str(carro[0][6]))
#Edita o cliente selecionado
def editar_cliente():
    global numero_id
    linha = listarclientes.tableWidget.currentRow()

    cursor = banco.cursor()
    cursor.execute("SELECT id_cliente FROM cliente")
    dados_recebidos = cursor.fetchall()
    valor_id = dados_recebidos[linha][0]
    cursor.execute("SELECT * FROM cliente WHERE id_cliente="+str(valor_id))
    produto = cursor.fetchall()
    editarcliente.show()

    numero_id = valor_id

    editarcliente.nome.setText(str(produto[0][1]))
    editarcliente.rg.setText(str(produto[0][2]))
    editarcliente.cpf.setText(str(produto[0][3]))
    editarcliente.email.setText(str(produto[0][4]))
    editarcliente.telefone.setText(str(produto[0][5]))
    editarcliente.endereco.setText(str(produto[0][6]))
    editarcliente.cep.setText(str(produto[0][7]))
#Locar/Vender Carro
def salvar_dados():
    categoriax = ''
    cpfcliente = telavenda.cpf.text()
    placacarro = telavenda.placa.text()


    if telavenda.alugueld.isChecked():
        categoriax="Aluguel Diario"
    elif telavenda.aluguelm.isChecked():
        categoriax="Aluguel Mensal"
    elif telavenda.compra.isChecked():
        categoriax="Venda"

    if categoriax == '':
        show_popup()
    else:
        venda = [cpfcliente, placacarro, categoriax]
        consulta(venda)


def consulta(venda):
    ##https://www.pythonprogressivo.net/2018/10/Como-Adicionar-Alterar-Retirar-Item-Dicionario.html
    sql = "SELECT * FROM carro"
    sql += " JOIN cliente ON cpf = " + venda[0]
    sql += " WHERE placa = '" + venda[1] + "'"

    cursor = banco.cursor()
    cursor.execute(sql)
    resultado = cursor.fetchall()

    if resultado != ():
        coluna = ''
        if venda[2] == "Aluguel Diario":
            coluna = resultado[0][4]
        elif venda[2]  == "Aluguel Mensal":
            coluna = resultado[0][5]
        elif venda[2]  == "Venda":
            coluna = resultado[0][6]

        sql = "INSERT INTO vendas (cpf, placa, valor) VALUES (%s,%s,%s)"
        dados = (str(venda[0]), str(venda[1]), coluna)
        cursor.execute(sql, dados)
        banco.commit()
        telavenda.close()
        telaprincipal.show()
    else:
        venda_popup()

app = QtWidgets.QApplication([])

##Telas
telaprincipal = uic.loadUi(r'C:\Users\fabrica.aluno2\Documents\GitHub\fabrica-software\QT Designer\Aluguel de carros\telaopcoes.ui')
telavenda = uic.loadUi(r'C:\Users\fabrica.aluno2\Documents\GitHub\fabrica-software\QT Designer\Aluguel de carros\telavenda.ui')
cadastrocarros = uic.loadUi(r'C:\Users\fabrica.aluno2\Documents\GitHub\fabrica-software\QT Designer\Aluguel de carros\cadastrocarro.ui')
cadastrousuarios = uic.loadUi(r'C:\Users\fabrica.aluno2\Documents\GitHub\fabrica-software\QT Designer\Aluguel de carros\cadastrousuario.ui')
listarcarros = uic.loadUi(r'C:\Users\fabrica.aluno2\Documents\GitHub\fabrica-software\QT Designer\Aluguel de carros\listadecarros.ui')
listarclientes = uic.loadUi(r'C:\Users\fabrica.aluno2\Documents\GitHub\fabrica-software\QT Designer\Aluguel de carros\listadeclientes.ui')
editarcarro = uic.loadUi(r'C:\Users\fabrica.aluno2\Documents\GitHub\fabrica-software\QT Designer\Aluguel de carros\editarcarro.ui')
editarcliente = uic.loadUi(r'C:\Users\fabrica.aluno2\Documents\GitHub\fabrica-software\QT Designer\Aluguel de carros\editarcliente.ui')
confirmarpagamento = uic.loadUi(r'C:\Users\fabrica.aluno2\Documents\GitHub\fabrica-software\QT Designer\Aluguel de carros\confirmarpagamento.ui')
#Ações
telaprincipal.locarvcarro.clicked.connect(abrir_tela_venda)
telaprincipal.cadcarro.clicked.connect(abrir_cadastro_carros)
telaprincipal.cadcliente.clicked.connect(abrir_cadastro_clientes)
cadastrocarros.cadastrar.clicked.connect(cadastro_carro)
cadastrocarros.listar.clicked.connect(listar_carros)
cadastrousuarios.cadastrar.clicked.connect(cadastro_cliente)
cadastrousuarios.listar.clicked.connect(listar_clientes)
listarcarros.editar.clicked.connect(editar_carro)
listarcarros.deletar.clicked.connect(excluir_carro)
listarclientes.editar.clicked.connect(editar_cliente)
editarcarro.salvar.clicked.connect(salvar_carro_editado)
editarcliente.salvar.clicked.connect(salvar_cliente_editado)
telavenda.finalizar.clicked.connect(salvar_dados)

telaprincipal.show()
app.exec()

'''
Criar telas no QTDesigner
Instalar: pip install mysql-connector-python
pip install PyMySQL


Acessar no browser: //localhost/phpmyadmin

Criar banco de dados para realizar o exercício

CREATE DATABASE aluguelcarros

CREATE TABLE carro(
    id_carro INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    marca VARCHAR(50),
    descricao VARCHAR(100),
    placa VARCHAR(7),
    precodiaria DOUBLE,
    precomensal DOUBLE,
    precovenda DOUBLE
);

CREATE TABLE cliente(
    id_cliente INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    rg VARCHAR(9),
    cpf VARCHAR(11),
    email VARCHAR(30),
    telefone VARCHAR(30),
    endereco VARCHAR(50),
    cep VARCHAR(20)
);

CREATE TABLE vendas(
    id_venda INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    cpf VARCHAR(11),
    placa VARCHAR(7),
    valor VARCHAR(10),
    data TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP
);


https://www.youtube.com/watch?v=dy_SFTsUjDc
'''