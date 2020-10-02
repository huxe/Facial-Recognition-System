from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import cv2
import pandas as pd
import numpy as np
import Register as reg
import pred_face as prdf
import AddIp as AP

user=pd.read_csv('user.csv')

class Ui_frmLogin(object):
    def setupUi(self, frmLogin):
        frmLogin.setObjectName("frmLogin")
        frmLogin.resize(779, 499)
        frmLogin.setStyleSheet("background-color: white;")
        self.centralwidget = QtWidgets.QWidget(frmLogin)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 40, 365, 62))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("logo.PNG"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.btnLogin = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogin.setGeometry(QtCore.QRect(290, 260, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btnLogin.setFont(font)
        self.btnLogin.setStyleSheet("background-color: rgb(67, 174, 255);")
        self.btnLogin.setObjectName("btnLogin")
        self.btnRegister = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegister.setGeometry(QtCore.QRect(100, 390, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btnRegister.setFont(font)
        self.btnRegister.setStyleSheet("background-color:rgb(255, 118, 84);")
        self.btnRegister.setObjectName("btnRegister")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(420, 10, 361, 461))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("abstract-flat-face-recognition-background_23-2148175048.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(120, 350, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Century")
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(480, 430, 271, 16))
        self.label_6.setObjectName("label_6")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 160, 92, 71))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.txtEmail = QtWidgets.QTextEdit(self.centralwidget)
        self.txtEmail.setGeometry(QtCore.QRect(160, 161, 256, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtEmail.setFont(font)
        self.txtEmail.setObjectName("txtEmail")
        self.txtPassword = QtWidgets.QTextEdit(self.centralwidget)
        self.txtPassword.setGeometry(QtCore.QRect(160, 200, 256, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtPassword.setFont(font)
        self.txtPassword.setObjectName("txtPassword")
        frmLogin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(frmLogin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 779, 21))
        self.menubar.setObjectName("menubar")
        frmLogin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(frmLogin)
        self.statusbar.setObjectName("statusbar")
        frmLogin.setStatusBar(self.statusbar)

        self.retranslateUi(frmLogin)
        QtCore.QMetaObject.connectSlotsByName(frmLogin)

        self.btnRegister.clicked.connect(self.CallReg)
        # Click Login
        self.btnLogin.clicked.connect(self.Validation)
        # Click Registtratiom


    def CallReg(self):
        import sys
        reg.app = QtWidgets.QApplication(sys.argv)
        reg.frmLogin = QtWidgets.QMainWindow()
        reg.ui = reg.Ui_frmLogin()
        reg.ui.setupUi(reg.frmLogin)
        reg.frmLogin.show()


    def Validation(self):
        try:
            ind=np.where(user.values==self.txtEmail.toPlainText())[0][0]
            if self.txtPassword.toPlainText()==user.values[ind][1]:
                # self.hrcascade()
                import sys
                AP.app = QtWidgets.QApplication(sys.argv)
                AP.frmIpAdd = QtWidgets.QMainWindow()
                AP.ui = AP.Ui_frmIpAdd()
                AP.ui.setupUi(AP.frmIpAdd)
                AP.frmIpAdd.show()
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Password Dose not match")
                msg.exec_()
        except:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Something Wrong!")
            msg.exec_()


    def retranslateUi(self, frmLogin):
        _translate = QtCore.QCoreApplication.translate
        frmLogin.setWindowTitle(_translate("frmLogin", "Login Page"))
        self.btnLogin.setText(_translate("frmLogin", "LOGIN"))
        self.btnRegister.setText(_translate("frmLogin", "Register Yourself!!"))
        self.label_5.setText(_translate("frmLogin", "Dont Have Account??"))
        self.label_6.setText(_translate("frmLogin", "© Third Mind Tecnology. 2020. All rights reserved."))
        self.label_2.setText(_translate("frmLogin", "Email"))
        self.label_3.setText(_translate("frmLogin", "Password"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmLogin = QtWidgets.QMainWindow()
    ui = Ui_frmLogin()
    ui.setupUi(frmLogin)
    frmLogin.show()
    sys.exit(app.exec_())
