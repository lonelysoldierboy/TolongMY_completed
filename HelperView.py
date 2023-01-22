# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 04:21:58 2023

@author: 60122
"""

from PyQt5 import QtCore, QtGui, QtWidgets
import folium
import webbrowser
from TolongMYPrototype import latitude,longitude
import sqlite3
from selenium import webdriver
class Ui_HelperView(object):
    def __init__(self,ID):
        self.id=ID
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
    def UpdateLocation(self):
        id = self.id
        conn = sqlite3.connect("MapList.db")
        cursor=conn.cursor()
        cursor.execute("DELETE FROM Helpers WHERE id=?",(self.id,))
        
        driver = webdriver.Chrome(r'C:\Users\60122\Documents\webdriver\chromedriver.exe')
        url = "https://whatmylocation.com/"
        driver.get(url)
        latitude = driver.find_element("xpath" , '//*[@id="latitude"]')
        longitude = driver.find_element("xpath", '//*[@id="longitude"]')
        
        cursor.execute('''INSERT INTO Helpers(
           id, NAME, LATITUDE, LONGITUDE) VALUES 
           (?,?,?,?)''',(id,'HELPER',latitude.text,longitude.text))
        conn.commit()
        conn.close()
        
        
    def setupUi(self, HelperView):
        HelperView.setObjectName("HelperView")
        HelperView.resize(277, 141)
        self.centralwidget = QtWidgets.QWidget(HelperView)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.openMap())
        self.pushButton.setGeometry(QtCore.QRect(80, 40, 141, 23))
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.UpdateLocation())
        self.pushButton_2.setGeometry(QtCore.QRect(80, 70, 141, 23))
        self.pushButton_2.setObjectName("pushButton")
        
        HelperView.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(HelperView)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 277, 22))
        self.menubar.setObjectName("menubar")
        HelperView.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(HelperView)
        self.statusbar.setObjectName("statusbar")
        HelperView.setStatusBar(self.statusbar)

        self.retranslateUi(HelperView)
        QtCore.QMetaObject.connectSlotsByName(HelperView)

    def retranslateUi(self, HelperView):
        _translate = QtCore.QCoreApplication.translate
        HelperView.setWindowTitle(_translate("HelperView", "MainWindow"))
        self.pushButton.setText(_translate("HelperView", "View Map"))
        self.pushButton_2.setText(_translate("HelperView", "Update Location"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HelperView = QtWidgets.QMainWindow()
    ui = Ui_HelperView("")
    ui.setupUi(HelperView)
    HelperView.show()
    sys.exit(app.exec_())