import pred_face as prdf
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import cv2 as cv2_2
class Ui_frmIpAdd(object):
    def setupUi(self, frmIpAdd):
        frmIpAdd.setObjectName("frmIpAdd")
        frmIpAdd.resize(418, 525)
        frmIpAdd.setStyleSheet("background-color: white;")
        self.centralwidget = QtWidgets.QWidget(frmIpAdd)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.txtIp = QtWidgets.QTextEdit(self.centralwidget)
        self.txtIp.setGeometry(QtCore.QRect(30, 60, 241, 31))
        self.txtIp.setObjectName("txtIp")
        self.btnAddIp = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddIp.setGeometry(QtCore.QRect(300, 60, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnAddIp.setFont(font)
        self.btnAddIp.setStyleSheet("background-color: rgb(181, 255, 147);")
        self.btnAddIp.setObjectName("btnAddIp")
        self.tblTime = QtWidgets.QTableView(self.centralwidget)
        self.tblTime.setGeometry(QtCore.QRect(10, 170, 401, 311))
        self.tblTime.setObjectName("tblTime")
        self.btnAddIp2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddIp2.setGeometry(QtCore.QRect(300, 110, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnAddIp2.setFont(font)
        self.btnAddIp2.setStyleSheet("background-color: rgb(181, 255, 147);")
        self.btnAddIp2.setObjectName("btnAddIp2")
        self.txtIp2 = QtWidgets.QTextEdit(self.centralwidget)
        self.txtIp2.setGeometry(QtCore.QRect(30, 110, 241, 31))
        self.txtIp2.setObjectName("txtIp2")
        frmIpAdd.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(frmIpAdd)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 418, 21))
        self.menubar.setObjectName("menubar")
        frmIpAdd.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(frmIpAdd)
        self.statusbar.setObjectName("statusbar")
        frmIpAdd.setStatusBar(self.statusbar)

        self.retranslateUi(frmIpAdd)
        QtCore.QMetaObject.connectSlotsByName(frmIpAdd)
        
        self.btnAddIp.clicked.connect(self.hrcascade)
        self.btnAddIp2.clicked.connect(self.hrcascade2)

    def retranslateUi(self, frmIpAdd):
        _translate = QtCore.QCoreApplication.translate
        frmIpAdd.setWindowTitle(_translate("frmIpAdd", "Add IP"))
        self.label.setText(_translate("frmIpAdd", "Add IP Address Example: http://192.168.2.102:8080"))
        self.btnAddIp.setText(_translate("frmIpAdd", "ADD"))
        self.btnAddIp2.setText(_translate("frmIpAdd", "ADD"))

    def hrcascade(self):
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        # cap = cv2.VideoCapture(0)
        # for external Ip camera
        cap = cv2.VideoCapture(self.txtIp.toPlainText()+'/video')
        model=prdf.LoadModel()
        name=None
        check=''
        while True:
            _, img = cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)
            
            for (x, y, w, h) in faces:
                name=prdf.runModel(model,img)
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
                cv2.putText(img,name,(x,y),cv2.FONT_HERSHEY_DUPLEX,1,(255,0,0),3)
            img=cv2.resize(img,(550,350))
            cv2.imshow('img', img)
            if check != name and name != None:
                print(name)
                check=name
            
            k = cv2.waitKey(30) & 0xff
            if k==27:
                break
        cap.release()

    def hrcascade2(self):
        face_cascade2 = cv2_2.CascadeClassifier('haarcascade_frontalface_default2.xml')
        # cap2 = cv2.VideoCapture(0)
        # for external Ip camera
        cap2 = cv2_2.VideoCapture(self.txtIp2.toPlainText()+'/video')
        model2=prdf.LoadModel()
        name2=None
        check2=''
        while True:
            _, img2 = cap2.read()
            gray2 = cv2_2.cvtColor(img2, cv2_2.COLOR_BGR2GRAY)
            faces2 = face_cascade2.detectMultiScale(gray2, 1.1, 4)
            
            for (x2, y2, w2, h2) in faces2:
                name2=prdf.runModel(model2,img2)
                cv2_2.rectangle(img2, (x2, y2), (x2+w2, y2+h2), (255, 0, 0), 2)
                cv2_2.putText(img2,name2,(x2,y2),cv2_2.FONT_HERSHEY_DUPLEX,1,(255,0,0),3)
            img2=cv2_2.resize(img2,(550,350))
            cv2_2.imshow('img2', img2)
            if check2 != name2 and name2 != None:
                print(name2)
                check2=name2
            
            k2 = cv2_2.waitKey(30) & 0xff
            if k2==27:
                break
        cap2.release()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmIpAdd = QtWidgets.QMainWindow()
    ui = Ui_frmIpAdd()
    ui.setupUi(frmIpAdd)
    frmIpAdd.show()
    sys.exit(app.exec_())
