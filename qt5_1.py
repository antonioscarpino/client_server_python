import subprocess
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_root(object):
    def setupUi(self, root):
        root.setObjectName("root")
        root.setEnabled(True)
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
        self.textBrowser.setObjectName("textBrowser")
        self.comando = QtWidgets.QLineEdit(self.centralwidget)
        self.comando.setGeometry(QtCore.QRect(160, 510, 431, 31))
        self.comando.setObjectName("comando")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(30, 515, 121, 21))
        self.label1.setObjectName("label1")
        root.setCentralWidget(self.centralwidget)

        self.retranslateUi(root)
        self.comando.returnPressed.connect(self.getText)
        QtCore.QMetaObject.connectSlotsByName(self.textBrowser)

    def retranslateUi(self, root):
        _translate = QtCore.QCoreApplication.translate
        root.setWindowTitle(_translate("root", "Prova Applicazione Qt5"))
        self.Button1.setText(_translate("root", "Connetti al Server"))
        self.label1.setText(_translate("root", "Inserisci un comando"))

    def getText(self):
        cmd = self.comando.text()
        if cmd == "exit":
            sys.exit(0)
        else:
            text = subprocess.run(
                cmd, shell=True, stdout=subprocess.PIPE,
                stderr=subprocess.PIPE, encoding="UTF-8")
            self.textBrowser.append(
                "Comando Richiesto -> " + cmd + "\n\n" + text.stdout + text.stderr)
            self.comando.clear()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    root = QtWidgets.QMainWindow()
    ui = Ui_root()
    ui.setupUi(root)
    root.show()
    sys.exit(app.exec_())
