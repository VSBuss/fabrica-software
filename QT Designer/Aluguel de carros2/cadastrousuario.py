# Form implementation generated from reading ui file 'cadastrousuario.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 631)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 0, 751, 620))
        self.frame.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 0, 127);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.nome = QtWidgets.QLineEdit(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nome.setFont(font)
        self.nome.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nome.setObjectName("nome")
        self.verticalLayout.addWidget(self.nome)
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.rg = QtWidgets.QLineEdit(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rg.setFont(font)
        self.rg.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.rg.setObjectName("rg")
        self.verticalLayout.addWidget(self.rg)
        self.label_7 = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.cpf_2 = QtWidgets.QLineEdit(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cpf_2.setFont(font)
        self.cpf_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cpf_2.setObjectName("cpf_2")
        self.verticalLayout.addWidget(self.cpf_2)
        self.label_4 = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.email = QtWidgets.QLineEdit(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.email.setFont(font)
        self.email.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.email.setObjectName("email")
        self.verticalLayout.addWidget(self.email)
        self.label_6 = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.telefone = QtWidgets.QLineEdit(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.telefone.setFont(font)
        self.telefone.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.telefone.setObjectName("telefone")
        self.verticalLayout.addWidget(self.telefone)
        self.label_9 = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.endereco = QtWidgets.QLineEdit(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.endereco.setFont(font)
        self.endereco.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.endereco.setObjectName("endereco")
        self.verticalLayout.addWidget(self.endereco)
        self.label_10 = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.cep = QtWidgets.QLineEdit(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cep.setFont(font)
        self.cep.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cep.setObjectName("cep")
        self.verticalLayout.addWidget(self.cep)
        self.cadastrar = QtWidgets.QPushButton(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.cadastrar.setFont(font)
        self.cadastrar.setStyleSheet("color: rgb(85, 0, 127);\n"
"background-color: rgb(255, 255, 255);")
        self.cadastrar.setObjectName("cadastrar")
        self.verticalLayout.addWidget(self.cadastrar)
        self.listar = QtWidgets.QPushButton(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.listar.setFont(font)
        self.listar.setStyleSheet("color: rgb(85, 0, 127);\n"
"background-color: rgb(255, 255, 255);")
        self.listar.setObjectName("listar")
        self.verticalLayout.addWidget(self.listar)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Cadastro de Usuários"))
        self.label_2.setText(_translate("MainWindow", "Nome completo:"))
        self.label_3.setText(_translate("MainWindow", "RG:"))
        self.label_7.setText(_translate("MainWindow", "CPF:"))
        self.label_4.setText(_translate("MainWindow", "E-mail:"))
        self.label_6.setText(_translate("MainWindow", "Telefone:"))
        self.label_9.setText(_translate("MainWindow", "Endereço:"))
        self.label_10.setText(_translate("MainWindow", "CEP:"))
        self.cadastrar.setText(_translate("MainWindow", "CADASTRAR"))
        self.listar.setText(_translate("MainWindow", "LISTAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
