# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 03:59:27 2023

@author: 60122
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from Victim import Ui_VictimWindow
from HelperView import Ui_HelperView
from TolongMYPrototype import latitude,longitude
import sqlite3

class Ui_MainWindow(object):
    def open_Victim(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_VictimWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def open_Helper(self):
        conn =sqlite3.connect('MapList.db')
        cursor=conn.cursor()
        
        cursor.execute('''SELECT NAME from Helpers''')
        NAME = cursor.fetchall()
        
        self.i=len(NAME)+1
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HelperView(self.i)
        self.ui.setupUi(self.window)
        self.window.show()
        
        
        cursor.execute('''INSERT INTO Helpers(
           id,Name,Latitude, Longitude) VALUES 
           (?,?,?,?)''',(self.i,'HELPER',latitude.text,longitude.text))
        conn.commit()
        conn.close()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(725, 424)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.open_Victim())
        self.pushButton.setGeometry(QtCore.QRect(220, 120, 311, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.open_Helper())
        self.pushButton_2.setGeometry(QtCore.QRect(220, 200, 311, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 40, 360, 50))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 725, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "VICTIM"))
        self.pushButton_2.setText(_translate("MainWindow", "HELPER"))
        self.label.setText(_translate("MainWindow", "TOLONG MY"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())