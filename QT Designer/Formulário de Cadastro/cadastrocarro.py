# Form implementation generated from reading ui file 'cadastrocarro.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(903, 636)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 20, 858, 224))
        self.frame.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 0, 127);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.dateEdit = QtWidgets.QDateEdit(parent=self.frame)
        self.dateEdit.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 1, 8, 1, 2)
        self.cpf = QtWidgets.QLineEdit(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cpf.setFont(font)
        self.cpf.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cpf.setObjectName("cpf")
        self.gridLayout.addWidget(self.cpf, 2, 2, 1, 2)
        self.label_9 = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)
        self.cep = QtWidgets.QLineEdit(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cep.setFont(font)
        self.cep.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cep.setObjectName("cep")
        self.gridLayout.addWidget(self.cep, 4, 1, 1, 2)
        self.endereco = QtWidgets.QLineEdit(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.endereco.setFont(font)
        self.endereco.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.endereco.setObjectName("endereco")
        self.gridLayout.addWidget(self.endereco, 3, 2, 1, 2)
        self.dateEdit_3 = QtWidgets.QDateEdit(parent=self.frame)
        self.dateEdit_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.gridLayout.addWidget(self.dateEdit_3, 2, 8, 1, 2)
        self.label_12 = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 3, 4, 1, 3)
        self.comboBox = QtWidgets.QComboBox(parent=self.frame)
        self.comboBox.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 4, 4, 1, 1)
        self.label_8 = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 4, 5, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)
        self.rg_2 = QtWidgets.QLineEdit(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rg_2.setFont(font)
        self.rg_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.rg_2.setObjectName("rg_2")
        self.gridLayout.addWidget(self.rg_2, 4, 6, 1, 2)
        self.label_10 = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 4, 8, 1, 1)
        self.nome = QtWidgets.QLineEdit(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nome.setFont(font)
        self.nome.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nome.setObjectName("nome")
        self.gridLayout.addWidget(self.nome, 1, 2, 1, 2)
        self.label_4 = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 4, 1, 2)
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 2)
        self.label_11 = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 2, 4, 1, 2)
        self.dateEdit_2 = QtWidgets.QDateEdit(parent=self.frame)
        self.dateEdit_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.gridLayout.addWidget(self.dateEdit_2, 3, 8, 1, 2)
        self.cadastrar = QtWidgets.QPushButton(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.cadastrar.setFont(font)
        self.cadastrar.setStyleSheet("color: rgb(85, 0, 127);\n"
"background-color: rgb(255, 255, 255);")
        self.cadastrar.setObjectName("cadastrar")
        self.gridLayout.addWidget(self.cadastrar, 5, 6, 1, 4)
        self.rg = QtWidgets.QLineEdit(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rg.setFont(font)
        self.rg.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.rg.setObjectName("rg")
        self.gridLayout.addWidget(self.rg, 4, 9, 1, 1)
        self.label_13 = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 5, 0, 1, 2)
        self.comboBox_2 = QtWidgets.QComboBox(parent=self.frame)
        self.comboBox_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 5, 2, 1, 2)
        self.label = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 4, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_9.setText(_translate("MainWindow", "Cor:"))
        self.label_7.setText(_translate("MainWindow", "Ano:"))
        self.label_12.setText(_translate("MainWindow", "venc licensiamento:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Gasolina"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Álcool"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Diesel"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Flex"))
        self.label_8.setText(_translate("MainWindow", "Placa:"))
        self.label_2.setText(_translate("MainWindow", "Marca:"))
        self.label_10.setText(_translate("MainWindow", "UF:"))
        self.label_4.setText(_translate("MainWindow", "Combustivel:"))
        self.label_6.setText(_translate("MainWindow", "venc IPVA:"))
        self.label_3.setText(_translate("MainWindow", "Modelo:"))
        self.label_11.setText(_translate("MainWindow", "venc DPVAT:"))
        self.cadastrar.setText(_translate("MainWindow", "CADASTRAR"))
        self.label_13.setText(_translate("MainWindow", "Categoria:"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Aluguel Diário"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Aluguel Mensal"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Venda"))
        self.label.setText(_translate("MainWindow", "Cadastro de Carros"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
