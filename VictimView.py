# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 04:02:10 2023

@author: 60122
"""

from PyQt5 import QtCore, QtGui, QtWidgets
import folium
import sqlite3
import webbrowser
from TolongMYPrototype import latitude,longitude
from Victim import *
from selenium import webdriver
def getIC():
    return
class Ui_MainWindow(object):
    def __init__(self,IC,Name,Phone):
        self.IC=IC
        self.Name=Name
        self.Phone=Phone
    def openMap(self):
        l1 = []
        l2 = []
        l3 = []
        l4 = []
        l5 = []
        l6 = []
        conn1 = sqlite3.connect('MapList.db')
        cursor = conn1.cursor()
        cursor.execute('''SELECT LATITUDE from Victims''')
        Lat = cursor.fetchall()
        cursor.execute('''SELECT  LONGITUDE from Victims''')
        Lng = cursor.fetchall()
        cursor.execute('''SELECT NAME from Victims''')
        NAME = cursor.fetchall()
        
        
        cursor.execute('''SELECT LATITUDE from Helpers''')
        HLat = cursor.fetchall()
        cursor.execute('''SELECT  LONGITUDE from Helpers''')
        HLng = cursor.fetchall()
        cursor.execute('''SELECT NAME from Helpers''')
        HNAME = cursor.fetchall()
        
        print(Lat,Lng,NAME) 
        for s in Lat:
            for r in s:
                l1.append(float(r))
                
        for m in Lng:        
            for q in m:
                l2.append(float(q))
        for e in NAME:        
            for n in e:
                l3.append(str(n))
        
        for s in HLat:
            for r in s:
                l4.append(float(r))
                
        for m in HLng:        
            for q in m:
                l5.append(float(q))
        for e in HNAME:        
            for n in e:
                l6.append(str(n))
                
        print(l1)
        print(l2)
        print(l3)
        print(l4)
        print(l5)
        print(l6)
        conn1.close()
        myMap = folium.Map(location=[float(latitude.text),float(longitude.text)],zoom_start=9)

        for d in range(len(l1)):
            print(l3[d],l1[d],l2[d])
            folium.Marker([l1[d],l2[d]],popup=(l3[d]),icon=folium.Icon(color='darkred')).add_to((myMap)) 
        for e in range(len(l4)):
            print(l4[e],l5[e],l6[e])
            folium.Marker([l4[e],l5[e]],popup=(l6[e]),icon=folium.Icon(color='green',icon_color='black')).add_to((myMap)) 
        myMap.save("Map.html") 
        webbrowser.open_new_tab("Map.html")
    def deleteFromMap(self):
       conn = sqlite3.connect("MapList.db")
       cursor=conn.cursor()
       cursor.execute("DELETE FROM Victims WHERE IC=?",(self.IC,))
       conn.commit()
       conn.close()
    def updateLocation(self):
        conn = sqlite3.connect("MapList.db")
        cursor=conn.cursor()
        cursor.execute("DELETE FROM Victims WHERE IC=?",(self.IC,))
        
        driver = webdriver.Chrome(r'C:\Users\60122\Documents\webdriver\chromedriver.exe')
        url = "https://whatmylocation.com/"
        driver.get(url)
        latitude = driver.find_element("xpath" , '//*[@id="latitude"]')
        longitude = driver.find_element("xpath", '//*[@id="longitude"]')
        
        cursor.execute('''INSERT INTO Victims(
           IC, Name, Number, Latitude, Longitude) VALUES 
           (?,?,?,?,?)''',(self.IC,self.Name,self.Phone,latitude.text,longitude.text))
        conn.commit()
        conn.close()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(257, 150)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.openMap())
        self.pushButton_2.setGeometry(QtCore.QRect(60, 20, 141, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.deleteFromMap())
        self.pushButton.setGeometry(QtCore.QRect(60, 60, 141, 23))
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.updateLocation())
        self.pushButton_3.setGeometry(QtCore.QRect(60, 100, 141, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 257, 22))
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
        self.pushButton_2.setText(_translate("MainWindow", "View Map"))
        self.pushButton.setText(_translate("MainWindow", "I have been saved"))
        self.pushButton_3.setText(_translate("MainWindow", "Update my location"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow("","","")
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())