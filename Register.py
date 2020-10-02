# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Register.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from csv import writer
from PyQt5.QtWidgets import QMessageBox


class Ui_frmLogin(object):
    def setupUi(self, frmLogin):
        frmLogin.setObjectName("frmLogin")
        frmLogin.resize(447, 438)
        frmLogin.setStyleSheet("background-color: white;")
        self.centralwidget = QtWidgets.QWidget(frmLogin)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 30, 301, 51))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("logo2.JPG"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txtEmail = QtWidgets.QTextEdit(self.centralwidget)
        self.txtEmail.setGeometry(QtCore.QRect(130, 110, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtEmail.setFont(font)
        self.txtEmail.setObjectName("txtEmail")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.txtPassword = QtWidgets.QTextEdit(self.centralwidget)
        self.txtPassword.setGeometry(QtCore.QRect(130, 160, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtPassword.setFont(font)
        self.txtPassword.setObjectName("txtPassword")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 210, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.txtReEnter = QtWidgets.QTextEdit(self.centralwidget)
        self.txtReEnter.setGeometry(QtCore.QRect(130, 210, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtReEnter.setFont(font)
        self.txtReEnter.setObjectName("txtReEnter")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 260, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.txtPhoneNo = QtWidgets.QTextEdit(self.centralwidget)
        self.txtPhoneNo.setGeometry(QtCore.QRect(130, 260, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtPhoneNo.setFont(font)
        self.txtPhoneNo.setObjectName("txtPhoneNo")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 310, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.txtAddress = QtWidgets.QTextEdit(self.centralwidget)
        self.txtAddress.setGeometry(QtCore.QRect(130, 310, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtAddress.setFont(font)
        self.txtAddress.setObjectName("txtAddress")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(0, -60, 451, 561))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("a.JPG"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.btnRegister = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegister.setGeometry(QtCore.QRect(130, 350, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btnRegister.setFont(font)
        self.btnRegister.setStyleSheet("background-color: rgb(79, 185, 255);")
        self.btnRegister.setObjectName("btnRegister")
        self.label_7.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.txtEmail.raise_()
        self.label_3.raise_()
        self.txtPassword.raise_()
        self.label_4.raise_()
        self.txtReEnter.raise_()
        self.label_5.raise_()
        self.txtPhoneNo.raise_()
        self.label_6.raise_()
        self.txtAddress.raise_()
        self.btnRegister.raise_()
        frmLogin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(frmLogin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 447, 21))
        self.menubar.setObjectName("menubar")
        frmLogin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(frmLogin)
        self.statusbar.setObjectName("statusbar")
        frmLogin.setStatusBar(self.statusbar)

        self.retranslateUi(frmLogin)
        QtCore.QMetaObject.connectSlotsByName(frmLogin)
                # click register button
        self.btnRegister.clicked.connect(self.RegClick)

    def retranslateUi(self, frmLogin):
        _translate = QtCore.QCoreApplication.translate
        frmLogin.setWindowTitle(_translate("frmLogin", "Register"))
        self.label_2.setText(_translate("frmLogin", "Email"))
        self.label_3.setText(_translate("frmLogin", "Password"))
        self.label_4.setText(_translate("frmLogin", "Re-enter"))
        self.label_5.setText(_translate("frmLogin", "Phone No"))
        self.label_6.setText(_translate("frmLogin", "Address"))
        self.btnRegister.setText(_translate("frmLogin", "Register Now"))

    def RegClick(self):
        if self.txtPassword .toPlainText()==self.txtReEnter.toPlainText():
            # List of strings
            row_contents = [self.txtEmail.toPlainText(),self.txtPassword.toPlainText(),self.txtPhoneNo.toPlainText(),self.txtAddress.toPlainText()]
            self.append_list_as_row('user.csv', row_contents)
            msg = QMessageBox()
            msg.setWindowTitle("Reg")
            msg.setText("Congrats you registerd")
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Password Dose not match")
            msg.exec_()

    def append_list_as_row(self,file_name, list_of_elem):
        with open(file_name, 'a+', newline='') as write_obj:
            csv_writer = writer(write_obj)
            csv_writer.writerow(list_of_elem)
            write_obj.close()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmLogin = QtWidgets.QMainWindow()
    ui = Ui_frmLogin()
    ui.setupUi(frmLogin)
    frmLogin.show()
    sys.exit(app.exec_())
def run():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmLogin = QtWidgets.QMainWindow()
    ui = Ui_frmLogin()
    ui.setupUi(frmLogin)
    frmLogin.show()

