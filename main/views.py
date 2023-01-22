import sqlite3
from django.shortcuts import render
from .forms import VictimForm
from selenium import webdriver
from django.http import HttpResponseRedirect
import folium
import webbrowser
# Create your views here.
def main(request):
    return render(request, 'index.html')

def helper(request):
        conn =sqlite3.connect('MapList.db')
        cursor=conn.cursor()
        
        cursor.execute('''SELECT NAME from Helpers''')
        NAME = cursor.fetchall()
        id=len(NAME)+1
        driver = webdriver.Chrome(r'C:\Users\Asus\Desktop\bantumy\chromedriver.exe')
        url = "https://whatmylocation.com/"
        driver.get(url)
        latitude = driver.find_element("xpath" , '//*[@id="latitude"]')
        longitude = driver.find_element("xpath", '//*[@id="longitude"]')
        cursor.execute('''INSERT INTO Helpers(
           id,Name,Latitude, Longitude) VALUES 
           (?,?,?,?)''',(id,'HELPER',latitude.text,longitude.text))
        conn.commit()
        conn.close()
        if request.method == 'POST' and 'show_map_helper' in request.POST:
            lx=[]
            conn = sqlite3.connect("MapList.db")
            cursor=conn.cursor()
            cursor.execute('''SELECT id from Helpers''')
            id = cursor.fetchall()
            for m in id:        
                for q in m:
                    lx.append(q)
            cursor.execute("DELETE FROM Helpers WHERE id=?",(lx[-1],))
            l1 = []
            l2 = []
            l3 = []
            l4 = []
            l5 = []
            l6 = []
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
                    
            conn.commit()
            conn.close()
            myMap = folium.Map(location=[float(latitude.text),float(longitude.text)],zoom_start=9)

            for d in range(len(l1)):
                print(l3[d],l1[d],l2[d])
                folium.Marker([l1[d],l2[d]],popup=(l3[d]),icon=folium.Icon(color='darkred')).add_to((myMap)) 
            for e in range(len(l4)):
                print(l4[e],l5[e],l6[e])
                folium.Marker([l4[e],l5[e]],popup=(l6[e]),icon=folium.Icon(color='green',icon_color='black')).add_to((myMap)) 
            myMap.save("Map.html") 
            webbrowser.open_new_tab("Map.html")
        elif request.method == 'POST' and 'update_helper' in request.POST:
            l2=[]
            conn = sqlite3.connect("MapList.db")
            cursor=conn.cursor()
            cursor.execute('''SELECT id from Helpers''')
            id = cursor.fetchall()
            for m in id:        
                for q in m:
                    l2.append(q)
            cursor.execute("DELETE FROM Helpers WHERE id=?",(l2[-1],))
            driver = webdriver.Chrome(r'C:\Users\60122\Documents\webdriver\chromedriver.exe')
            url = "https://whatmylocation.com/"
            driver.get(url)
            latitude = driver.find_element("xpath" , '//*[@id="latitude"]')
            longitude = driver.find_element("xpath", '//*[@id="longitude"]')
            cursor.execute('''INSERT INTO Helpers(
           id,Name,Latitude, Longitude) VALUES 
           (?,?,?,?)''',(l2[-1],'HELPER',latitude.text,longitude.text))
            conn.commit()
            conn.close()
        return render(request, 'helper.html')

def victim(request):
    if request.method == "POST":
        form = VictimForm(request.POST or None)
        if form.is_valid():
            form.save()
            driver = webdriver.Chrome(r'C:\Users\Asus\Desktop\bantumy\chromedriver.exe')
            url = "https://whatmylocation.com/"
            driver.get(url)
            latitude = driver.find_element("xpath" , '//*[@id="latitude"]')
            longitude = driver.find_element("xpath", '//*[@id="longitude"]')
            name = form.cleaned_data["name"]
            ic = form.cleaned_data["ic"]
            number = form.cleaned_data["number"]

            conn = sqlite3.connect("MapList.db")
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO Victims(
           IC, Name, Number, Latitude, Longitude) VALUES 
           (?,?,?,?,?)''',(ic,name,number,latitude.text,longitude.text))
            conn.commit()
            conn.close()
            return HttpResponseRedirect('victimview')#nanti ubah ke map.html  
    else:
            return render(request, 'victim.html')


def victimview(request):
    if request.method == 'POST' and 'show_map' in request.POST:
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
       
        conn1.close()
        driver = webdriver.Chrome(r'C:\Users\60122\Documents\webdriver\chromedriver.exe')
        url = "https://whatmylocation.com/"
        driver.get(url)
        latitude = driver.find_element("xpath" , '//*[@id="latitude"]')
        longitude = driver.find_element("xpath", '//*[@id="longitude"]')
        myMap = folium.Map(location=[float(latitude.text),float(longitude.text)],zoom_start=9)

        for d in range(len(l1)):
            print(l3[d],l1[d],l2[d])
            folium.Marker([l1[d],l2[d]],popup=(l3[d]),icon=folium.Icon(color='darkred')).add_to((myMap)) 
        for e in range(len(l4)):
            print(l4[e],l5[e],l6[e])
            folium.Marker([l4[e],l5[e]],popup=(l6[e]),icon=folium.Icon(color='green',icon_color='black')).add_to((myMap)) 
        myMap.save("Map.html") 
        webbrowser.open_new_tab("Map.html")
    elif request.method == 'POST' and 'update' in request.POST:
        l1=[]
        l2=[]
        l3=[]
        conn = sqlite3.connect("MapList.db")
        cursor=conn.cursor()
        cursor.execute('''SELECT IC from Victims''')
        IC = cursor.fetchall()
        cursor.execute('''SELECT NAME from Victims''')
        NAME= cursor.fetchall()
        cursor.execute('''SELECT NUMBER from Victims''')
        NUMBER = cursor.fetchall()
        for m in IC:        
            for q in m:
                l1.append(q)
        for m in NAME:        
            for q in m:
                l2.append(q)
        for e in NUMBER:        
            for n in e:
                l3.append(str(n))
        cursor.execute("DELETE FROM Victims WHERE IC=?",(l1[-1],))
        driver = webdriver.Chrome(r'C:\Users\60122\Documents\webdriver\chromedriver.exe')
        url = "https://whatmylocation.com/"
        driver.get(url)
        latitude = driver.find_element("xpath" , '//*[@id="latitude"]')
        longitude = driver.find_element("xpath", '//*[@id="longitude"]')
        cursor.execute('''INSERT INTO Victims(
           IC, Name, Number, Latitude, Longitude) VALUES 
           (?,?,?,?,?)''',(l1[-1],l2[-1],l3[-1],latitude.text,longitude.text))
        conn.commit()
        conn.close()
    elif request.method == 'POST' and 'saved' in request.POST:
        l2=[]
        conn = sqlite3.connect("MapList.db")
        cursor=conn.cursor()
        cursor.execute('''SELECT IC from Victims''')
        IC = cursor.fetchall()
        for m in IC:        
            for q in m:
                l2.append(q)
        cursor.execute("DELETE FROM Victims WHERE IC=?",(l2[-1],))
        conn.commit()
        conn.close()
    return render(request,'victimview.html')