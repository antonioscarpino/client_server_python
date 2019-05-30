from PyQt5 import QtCore, QtGui, QtWidgets
import socket
import sys
import subprocess
import platform


class Ui_root(object):
    def setupUi(self, root):
        root.setObjectName("root")
        root.setEnabled(True)
        root.resize(1050, 600)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(root.sizePolicy().hasHeightForWidth())
        root.setSizePolicy(sizePolicy)
        root.setMinimumSize(QtCore.QSize(1050, 600))
        self.centralwidget = QtWidgets.QWidget(root)
        self.centralwidget.setObjectName("centralwidget")
        self.Button1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button1.setGeometry(QtCore.QRect(630, 500, 120, 45))
        self.Button1.setMinimumSize(QtCore.QSize(111, 0))
        self.Button1.setObjectName("Button1")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(25, 10, 1001, 430))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.comando = QtWidgets.QLineEdit(self.centralwidget)
        self.comando.setGeometry(QtCore.QRect(160, 510, 431, 31))
        self.comando.setObjectName("comando")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(30, 515, 121, 21))
        self.label1.setObjectName("label1")
        self.Button2 = QtWidgets.QPushButton(self.centralwidget)
        self.Button2.setGeometry(QtCore.QRect(770, 500, 120, 45))
        self.Button2.setMinimumSize(QtCore.QSize(111, 0))
        self.Button2.setObjectName("Button2")
        self.Button3 = QtWidgets.QPushButton(self.centralwidget)
        self.Button3.setGeometry(QtCore.QRect(910, 500, 120, 45))
        self.Button3.setMinimumSize(QtCore.QSize(111, 0))
        self.Button3.setObjectName("Button3")
        self.autore = QtWidgets.QLabel(self.centralwidget)
        self.autore.setGeometry(QtCore.QRect(900, 570, 130, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.autore.setFont(font)
        self.autore.setObjectName("autore")
        root.setCentralWidget(self.centralwidget)

        self.retranslateUi(root)
        self.Button1.clicked.connect(self.connetti)
        self.Button2.clicked.connect(self.disconnetti)
        self.Button3.clicked.connect(self.esci)
        self.comando.returnPressed.connect(self.getText)
        QtCore.QMetaObject.connectSlotsByName(root)

    def retranslateUi(self, root):
        _translate = QtCore.QCoreApplication.translate
        root.setWindowTitle(_translate("root", "Prova Applicazione Qt5"))
        self.Button1.setText(_translate("root", "Connetti al Server"))
        self.label1.setText(_translate("root", "Inserisci un comando"))
        self.Button2.setText(_translate("root", "Disconnetti il Server"))
        self.Button3.setText(_translate("root", "ESCI"))
        self.autore.setText(_translate("root", "Creato by Antonio Scarpino"))

    def connetti(self):
        try:
            sock = socket.socket()
            # Qui va inserito l'IP del Server e la porta sulla quale il Server é in ascolto
            sock.connect(("localhost", 15000))
            self.textBrowser.append(
                f"La connessione al Server: avvenuta con successo")
            self.sock = sock
        except socket.error as error:
            errore = (f"Connessione al Server non stabilita!! ERRORE: {error}")
            self.textBrowser.append(errore)
            sock.close()

    def disconnetti(self):
        if hasattr(self, 'sock'):
            self.sock.close()
            self.__delattr__('sock')
            self.textBrowser.append("Disconnessione dal Server avvenuta")
        else:
            self.textBrowser.append("Nessun Server ancora connesso")

    def esci(self):
        if hasattr(self, 'sock'):
            self.sock.close()
        sys.exit(0)

    def getText(self):
        cmd = self.comando.text()
        # print(cmd) # debug comando digitato
        if cmd == "exit":
            self.sock.close()
            sys.exit(0)
        elif cmd != "":
            if hasattr(self, 'sock'):
                self.sock.send(cmd.encode())
                data = self.sock.recv(4096)
                if platform.system() == "Linux":
                    self.textBrowser.append(
                        "Comando Richiesto -> " + cmd + "\n\n" + str(data, 'UTF-8'))
                    self.comando.clear()
                else:
                    self.textBrowser.append(
                        "Comando Richiesto -> " + cmd + "\n\n" + str(data, 'cp437'))
                    self.comando.clear()
            else:
                self.textBrowser.append(
                    "Non sei connesso ancora a nessun Server")
        else:
            self.textBrowser.append(
                "Inserisci un comando valido")
            self.comando.clear()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    root = QtWidgets.QMainWindow()
    ui = Ui_root()
    ui.setupUi(root)
    root.show()
    sys.exit(app.exec_())
