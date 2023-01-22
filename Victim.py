# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 04:00:48 2023

@author: 60122
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from TolongMYPrototype import latitude,longitude
from VictimView import *
import sqlite3

   
class Ui_VictimWindow(object):
    def SendInfo(self,vIC,vName,vPhone):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow(vIC,vName,vPhone)
        self.ui.setupUi(self.window)
        self.window.show()
        print(vIC,vName,vPhone,latitude.text,longitude.text)
        conn =sqlite3.connect('MapList.db')
        cursor=conn.cursor()
        
        cursor.execute('''SELECT NAME from Victims''')
        NAME = cursor.fetchall()
       
        
        cursor.execute('''INSERT INTO Victims(
           IC, Name, Number, Latitude, Longitude) VALUES 
           (?,?,?,?,?)''',(vIC,vName,vPhone,latitude.text,longitude.text))
        conn.commit()
        conn.close()
    def setupUi(self, VictimWindow):
        VictimWindow.setObjectName("VictimWindow")
        VictimWindow.resize(246, 204)
        self.centralwidget = QtWidgets.QWidget(VictimWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 71, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 111, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 91, 16))
        self.label_3.setObjectName("label_3")
        
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 221, 16))
        self.textEdit.setObjectName("lineEdit")
        
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 100, 151, 16))
        self.textEdit_2.setObjectName("textEdit_2")
        
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(10, 60, 221, 16))
        self.textEdit_3.setObjectName("textEdit_3")
        
        self.name = self.textEdit_2.toPlainText()
        self.ic=self.textEdit.toPlainText()
        self.phone = self.textEdit_3.toPlainText()
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.SendInfo(self.textEdit_3.toPlainText(),self.textEdit.toPlainText(),self.textEdit_2.toPlainText()))
        self.pushButton.setGeometry(QtCore.QRect(90, 130, 75, 23))
        self.pushButton.setObjectName("pushButton")
        VictimWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VictimWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 246, 22))
        self.menubar.setObjectName("menubar")
        VictimWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VictimWindow)
        self.statusbar.setObjectName("statusbar")
        VictimWindow.setStatusBar(self.statusbar)

        self.retranslateUi(VictimWindow)
        QtCore.QMetaObject.connectSlotsByName(VictimWindow)
        print(self.textEdit_3.toPlainText())
        return self.textEdit_3.toPlainText()
    def retranslateUi(self, VictimWindow):
        _translate = QtCore.QCoreApplication.translate
        VictimWindow.setWindowTitle(_translate("VictimWindow", "MainWindow"))
        self.label.setText(_translate("VictimWindow", "Name"))
        self.label_2.setText(_translate("VictimWindow", "IC / Passport Number"))
        self.label_3.setText(_translate("VictimWindow", "Phone Number"))
        self.pushButton.setText(_translate("VictimWindow", "Send"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VictimWindow = QtWidgets.QMainWindow()
    ui = Ui_VictimWindow()
    ui.setupUi(VictimWindow)
    VictimWindow.show()
    sys.exit(app.exec_())